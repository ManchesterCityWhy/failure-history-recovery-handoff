# Failure-History Recovery：新机项目交接

这个仓库只保存研究交接文档，不包含模型权重、实验数据、虚拟环境或已经部署好的代码。

## 最新入口：CFG 恢复实验（2026-11-12）

1. [给coding agent的启动说明](docs/CODING_AGENT_CFG_START_HERE.md)
2. [任务参考CFG：方法与实验计划](docs/CFG_RECOVERY_EXPERIMENT_PLAN_2026-11-12.md)

当前动作模型改为**冻结的LingBot-VA LIBERO-Long**。先检验以原任务T为参考、强化修正X的动作侧CFG，再检验失败历史的额外价值。11月10日已跑通12条普通指导WAM分支，但没有证明历史独有收益；**新的CFG推理尚未实现或执行**。

本轮以这两份新文档为准。仓库仍然只包含文档，不含CFG实现、模型权重、数据或可直接运行的环境。

## 历史交接（2026-11-07）

请完整阅读 [八卡5090项目交接书](docs/PROJECT_HANDOFF_8x5090_2026-11-07.md)。它可以独立指导一台空白机器从零开发，不依赖旧服务器、NFS、聊天记录或飞书。

重点章节：第0节总览，第5节真实结果与局限，第7节方法，第9节新机重建，第12节任务与门槛，第18节coding agent启动指令。

该交接书保留11月7日的完整研究背景与重建规格，其π0.5默认路线属于历史方案，不覆盖上面的最新LingBot-VA/CFG决定。旧工程和计划不能当作新机器已验证结果。

## 新机器如何接收

本仓库已按研究者要求公开。新机器无需登录GitHub，也不需要GitHub CLI、访问token或SSH key。

如果只需要最新CFG实验计划，直接下载一个Markdown文件：

```bash
curl -fL --retry 3 \
  https://raw.githubusercontent.com/ManchesterCityWhy/failure-history-recovery-handoff/main/docs/CFG_RECOVERY_EXPERIMENT_PLAN_2026-11-12.md \
  -o CFG_RECOVERY_EXPERIMENT_PLAN_2026-11-12.md
```

也可以匿名克隆整个文档仓库，保留README与校验文件：

```bash
git clone --depth 1 https://github.com/ManchesterCityWhy/failure-history-recovery-handoff.git
cd failure-history-recovery-handoff
sha256sum -c CHECKSUMS.sha256
```

仓库地址：<https://github.com/ManchesterCityWhy/failure-history-recovery-handoff>。

已经克隆过且没有本地改动时，在仓库根目录更新：

```bash
git pull --ff-only
sha256sum -c CHECKSUMS.sha256
```

如有本地改动，先保留并检查，不要强制覆盖或reset。macOS可将 `sha256sum` 换成 `shasum -a 256`。单独下载计划时，可按仓库的 `CHECKSUMS.sha256` 比较对应哈希。

首次只获取文档；模型和依赖按交接书在新机获取。不要把个人电脑的SSH私钥或登录凭据复制到共享服务器。

## 给coding agent的最短启动指令

> 请先完整阅读 docs/CODING_AGENT_CFG_START_HERE.md 和 docs/CFG_RECOVERY_EXPERIMENT_PLAN_2026-11-12.md。以最新冻结LingBot-VA路线为准，先实现三条件分支和阶段0的数值/KV缓存回归，通过后再做首个种子的22条试验，不直接启动66条或训练。这个仓库只有文档，不能假设已有实现、权重和旧数据；按目标机器条件独立重建，记录全部结果及限制。

## 仓库边界

- 仅文档交接，不表示全部旧资产已经迁移。
- 本仓库按研究者要求公开，包含拟议研究计划与历史路径；后续提交不要加入凭据、未授权资料、数据或权重。
- 旧路径只作历史证据定位，不能作为新机运行依赖。
- 新实验代码、权重和数据请在新机的独立研究目录中开发，依主文档另行版本管理。
