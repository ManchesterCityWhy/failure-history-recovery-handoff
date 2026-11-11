# Failure-History Recovery：项目交接

这个公开仓库保存研究交接文档、数据采集SOP、记录规范和候选seed生成器，不包含模型权重、原始实验数据、虚拟环境、CFG实现或已经部署好的仿真采集系统。

## 2026-11-12：两个工作入口

| 方向 | Coding agent入口 | 详细计划 |
|---|---|---|
| **本次交接：定向仿真数据集** | [CODING_AGENT_START.md](CODING_AGENT_START.md) | [数据SOP](docs/dataset_sop/2026-11-12/DATASET_SOP_V0.md) |
| 任务参考CFG方法实验 | [CFG启动说明](docs/CODING_AGENT_CFG_START_HERE.md) | [CFG方法与实验计划](docs/CFG_RECOVERY_EXPERIMENT_PLAN_2026-11-12.md) |

本次数据开发按数据SOP执行；方法实验按CFG计划执行。两个方向分别验证“历史中有没有额外信息”和“动作模型能否利用修正”。不能把指令执行改善当成历史价值，也不把两个方向的条件编号、预算和阶段混用。

### 数据工作

优先在成熟仿真平台上实现定向失败—恢复数据，保存从原任务开始、失败到恢复原任务的完整流程。先D1/P1物理小样，再补齐任务。

| 资料 | 用途 |
|---|---|
| [6张任务卡](docs/dataset_sop/2026-11-12/TASK_CATALOG_V0.md) | 搜索校准、掉落找回和进度修复 |
| [采集启动入口](docs/dataset_sop/2026-11-12/START_HERE.md) | 第一批任务及设计状态 |
| [机器可读配置](docs/dataset_sop/2026-11-12/collection_config_v0.json) | 72条开发、300条机制验证的配置 |
| [11-11总体研究计划](docs/benchmark_plan/2026-11-11/BENCHMARK_WORK_PLAN.md) | 研究边界、相关工作与论文规划 |
| [11-11已完成pilot报告](docs/pilot/2026-11-11/REPORT.md) | 实际结果、负结果和局限 |

新采集目标：12条冒烟（属于开发子集）→72条开发→300条冻结机制验证→通过门槛后扩量。300条由6模板×20核心场景组×2条件+60对照组成，尚未采集完成。576个候选条件配置只是采样计划，采样脚本不是仿真执行器，本次新增采集episode数为0。

已完成的受控搜索pilot有64条唯一历史、384次恢复执行，有限预算下观察到历史收益；普通32例中当前帧与历史指导均成功22例，没有历史特有增益。上限教师含规则/技能特权，不能据此声称通用自然失败恢复或新学习方法已经成功。

首批数据实施以11-12 SOP为准。11-11总体计划和11-07交接书保留背景，其数量与条件编号不覆盖数据SOP。旧服务器路径只作参考，不能假定新机可访问。

### 方法工作

CFG计划使用**冻结的官方LingBot-VA LIBERO-Long**，先检验以原任务T为参考、强化修正X的动作侧CFG，再检验失败历史的额外价值。源码与权重版本、三分支缓存要求、数值门槛和22→66条试验顺序见上述专门计划。

11月10日已跑通12条普通指导WAM分支，但没有证明历史独有收益；**新的CFG推理尚未实现或执行**。新机不得把伪代码、旧pilot或计划中的66条当成已运行的新结果。

## 历史背景：2026-11-07

[八卡5090项目交接书](docs/PROJECT_HANDOFF_8x5090_2026-11-07.md)保持原样，包含背景、旧结果、环境重建与完整研究方案。其π0.5默认路线属于历史方案；当前方法路线以CFG计划为准，当前数据实施以SOP为准。

## 远端如何接收

本仓库公开，无需登录GitHub，也不需要GitHub CLI、访问token或SSH key。

首次接收：

```bash
git clone --depth 1 https://github.com/ManchesterCityWhy/failure-history-recovery-handoff.git
cd failure-history-recovery-handoff
sha256sum -c CHECKSUMS.sha256
```

已经克隆且没有本地改动时，在仓库根目录执行：

```bash
git pull --ff-only
sha256sum -c CHECKSUMS.sha256
```

有本地改动时先保留并检查，不强制覆盖。macOS可将`sha256sum`换成`shasum -a 256`。

固定本次交接版本：

```bash
git clone --depth 1 --branch dataset-sop-2026-11-12-v0 \
  https://github.com/ManchesterCityWhy/failure-history-recovery-handoff.git \
  failure-history-recovery-sop-v0
```

如只需CFG计划，也可匿名下载：

```bash
curl -fL --retry 3 \
  https://raw.githubusercontent.com/ManchesterCityWhy/failure-history-recovery-handoff/main/docs/CFG_RECOVERY_EXPERIMENT_PLAN_2026-11-12.md \
  -o CFG_RECOVERY_EXPERIMENT_PLAN_2026-11-12.md
```

## 给coding agent的本次启动指令

> 请先完整阅读CODING_AGENT_START.md，再按docs/dataset_sop/2026-11-12/DATASET_SOP_V0.md开发定向仿真数据项目。先检查机器资源，优先D1/P1，完成12条冒烟和72条开发，通过门槛后做300条机制验证。采样脚本只有seed计划，采集器尚需开发。保留全部负例、错误与资源账目，不把计划当实际结果。方法实验另有CFG入口，勿混用编号或预算。

## 仓库边界

- 文档、schema和采样工具交接，不表示全部旧资产已经迁移。
- `PRIVATE`候选清单表示不应作为策略输入，不是账号凭据。本批是公开开发计划，不是保密论文测试集，也不是已执行数据。
- 新实验代码、权重和数据请在新机独立研究目录中开发，依相应计划另行版本管理。
- 不加入凭据、未授权资料、模型权重或原始数据；旧路径不能作为新机运行依赖。
