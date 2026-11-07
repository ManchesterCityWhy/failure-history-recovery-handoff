# Failure-History Recovery：新机项目交接

这个仓库只保存研究交接文档，不包含模型权重、实验数据、虚拟环境或已经部署好的代码。

## 主文档

请完整阅读 [八卡5090项目交接书](docs/PROJECT_HANDOFF_8x5090_2026-11-07.md)。它可以独立指导一台空白机器从零开发，不依赖旧服务器、NFS、聊天记录或飞书。

重点章节：第0节总览，第5节真实结果与局限，第7节方法，第9节新机重建，第12节任务与门槛，第18节coding agent启动指令。

当前状态：旧工程已跑通真实π0.5闭环与配对恢复，但尚未证明历史收益；拟议的恢复VLM与收益选择器尚未训练完成。不能将交接计划当作现成实现或论文正结果。

## 新机器如何接收

本仓库已按研究者要求公开。新机器无需登录GitHub，也不需要GitHub CLI、访问token或SSH key。

如果只需要交接书，直接下载一个Markdown文件：

```bash
curl -fL --retry 3 \
  https://raw.githubusercontent.com/ManchesterCityWhy/failure-history-recovery-handoff/main/docs/PROJECT_HANDOFF_8x5090_2026-11-07.md \
  -o PROJECT_HANDOFF_8x5090_2026-11-07.md
```

也可以匿名克隆整个文档仓库，保留README与校验文件：

```bash
git clone --depth 1 https://github.com/ManchesterCityWhy/failure-history-recovery-handoff.git
cd failure-history-recovery-handoff
sha256sum -c CHECKSUMS.sha256
```

仓库地址：<https://github.com/ManchesterCityWhy/failure-history-recovery-handoff>。

单独下载交接书时，可以检查其SHA256：

```bash
sha256sum PROJECT_HANDOFF_8x5090_2026-11-07.md
```

预期值为 `1904c9e1aadc79b6ebee575ab22b5045e89ba5a480a47e03fa73b511fb7d578e`。macOS可将 `sha256sum` 换成 `shasum -a 256`。

首次只获取文档；模型和依赖按交接书在新机获取。不要把个人电脑的SSH私钥或登录凭据复制到共享服务器。

## 给coding agent的最短启动指令

> 请完整阅读 docs/PROJECT_HANDOFF_8x5090_2026-11-07.md，按第18节启动。当前机器没有旧代码与实验记录，先从M0–M2完成环境、数据协议与可行性门槛；不要直接大规模训练。建议命令尚不存在，应先实现与测试。保留负例、错误、资源账目，不把计划或旧测试当作新机已验证结果。

## 仓库边界

- 仅文档交接，不表示全部旧资产已经迁移。
- 本仓库按研究者要求公开，包含拟议研究计划与历史路径；后续提交不要加入凭据、未授权资料、数据或权重。
- 旧路径只作历史证据定位，不能作为新机运行依赖。
- 新实验代码、权重和数据请在新机的独立研究目录中开发，依主文档另行版本管理。
