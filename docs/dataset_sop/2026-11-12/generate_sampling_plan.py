"""Create a private candidate/seed plan, not simulator data or executed results."""
import argparse
import hashlib
import json
import uuid
from pathlib import Path


def seed(master, *parts):
    payload = json.dumps([master, *parts], ensure_ascii=False, separators=(',', ':')).encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:4], 'big') & 0x7fffffff


def group_id(master, phase, task, kind, ordinal):
    return uuid.uuid5(uuid.NAMESPACE_URL, f'hr-data-v0:{master}:{phase}:{task}:{kind}:{ordinal}').hex


def build(config):
    master = config['master_seed']; rows = []
    for phase in ('development', 'frozen_validation'):
        spec = config[phase]
        for task_index, task in enumerate(config['task_ids']):
            groups = []
            for ordinal in range(spec['paired_group_candidates_per_task']):
                groups.append(('core', ordinal, [0, 1]))
            if phase == 'development':
                for kind_index, kind in enumerate(('V', 'U')):
                    condition = (task_index + kind_index) % 2
                    for ordinal in range(spec['control_candidates_per_target']):
                        groups.append((kind, ordinal, [condition]))
            else:
                for kind in ('V', 'U'):
                    per_condition = spec['control_candidates_per_task_per_condition'][kind]
                    # Each control is its own initialized world, alternating labels.
                    for ordinal in range(2 * per_condition):
                        groups.append((kind, ordinal, [ordinal % 2]))
            for kind, ordinal, conditions in groups:
                gid = group_id(master, phase, task, kind, ordinal)
                shared = {name: seed(master, phase, task, kind, ordinal, name)
                          for name in ('layout', 'appearance', 'fault_magnitude')}
                source = [seed(master, phase, task, kind, ordinal, 'source', trial)
                          for trial in range(config['source_sampling']['max_source_trials_per_candidate_condition'])]
                recovery = [seed(master, phase, task, kind, ordinal, 'recovery', trial)
                            for trial in config['recovery']['inference_seed_indices']]
                for condition in conditions:
                    cid = uuid.uuid5(uuid.NAMESPACE_URL, f'{gid}:condition:{condition}').hex
                    rows.append({'visibility': 'evaluator_private_not_policy_input',
                                 'status': 'PLANNED_NOT_EXECUTED', 'candidate_id': cid,
                                 'world_group_id': gid, 'phase': phase, 'task_id': task,
                                 'information_stratum': kind, 'candidate_ordinal': ordinal,
                                 'condition_slot_private': condition,
                                 'core_condition_meaning_private': config['condition_meaning'][task][condition] if kind == 'core' else None,
                                 'control_meaning_requires_task_card': kind != 'core',
                                 'shared_seeds': shared, 'source_trial_seeds': source,
                                 'recovery_seeds': recovery,
                                 'geometry_and_source_rng_do_not_depend_on_condition': True})
    return rows


def main(config_path, output):
    config_bytes = config_path.read_bytes(); config = json.loads(config_bytes)
    rows = build(config)
    assert not output.exists(), 'Version candidate plans instead of overwriting them'
    output.mkdir(parents=True)
    candidates = output / 'candidate_plan_PRIVATE.jsonl'
    candidates.write_text(''.join(json.dumps(row, ensure_ascii=False)+'\n' for row in rows))
    by_phase = {phase: sum(row['phase'] == phase for row in rows)
                for phase in ('development', 'frozen_validation')}
    receipt = {'status': 'sampling_plan_only_no_simulation_data',
               'config_sha256': hashlib.sha256(config_bytes).hexdigest(),
               'candidate_plan_sha256': hashlib.sha256(candidates.read_bytes()).hexdigest(),
               'candidate_condition_instances': len(rows), 'by_phase': by_phase,
               'max_source_attempts_if_all_candidates_run': len(rows)*config['source_sampling']['max_source_trials_per_candidate_condition'],
               'source_attempts_stop_by_prespecified_source_quota_not_recovery_outcome': True,
               'unique_failure_targets': {'development': config['development']['unique_failure_target'],
                                          'frozen_validation': config['frozen_validation']['unique_failure_target']},
               'actual_failed_episodes_collected': 0,
               'budget_and_templates_must_be_locked_before_validation_execution': True}
    (output / 'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('config', type=Path); parser.add_argument('output', type=Path)
    args = parser.parse_args(); main(args.config, args.output)
