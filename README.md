# Failure-History Recovery：新机项目交接

这个仓库只保存研究交接文档，不包含模型权重、实验数据、虚拟环境或已经部署好的代码。

## 主文档

请完整阅读 [八卡5090项目交接书](docs/PROJECT_HANDOFF_8x5090_2026-11-07.md)。它可以独立指导一台空白机器从零开发，不依赖旧服务器、NFS、聊天记录或飞书。

重点章节：第0节总览，第5节真实结果与局限，第7节方法，第9节新机重建，第12节任务与门槛，第18节coding agent启动指令。

当前状态：旧工程已跑通真实π0.5闭环与配对恢复，但尚未证明历史收益；拟议的恢复VLM与收益选择器尚未训练完成。不能将交接计划当作现成实现或论文正结果。

## 新机器如何接收

仓库保持私有。先在新机器安装Git与官方GitHub CLI，再用有仓库访问权的账号登录：

```bash
gh auth login --hostname github.com --git-protocol https --web
```

然后克隆本仓库：

```bash
gh auth setup-git
gh repo clone ManchesterCityWhy/failure-history-recovery-handoff
cd failure-history-recovery-handoff
```

仓库地址：<https://github.com/ManchesterCityWhy/failure-history-recovery-handoff>。

账号认证信息不要写进URL、脚本或交接文档，也不要把本机SSH私钥复制到新机器。首次只克隆文档；模型和依赖按交接书在新机获取。

下载后在仓库根目录校验交接书：

```bash
sha256sum -c CHECKSUMS.sha256
```

macOS可使用 `shasum -a 256 -c CHECKSUMS.sha256`。

如果不希望在共享开发机保存GitHub登录，可在已登录的个人电脑上下载仓库，再通过自己的安全文件传输通道复制文档到服务器。

## 给coding agent的最短启动指令

> 请完整阅读 docs/PROJECT_HANDOFF_8x5090_2026-11-07.md，按第18节启动。当前机器没有旧代码与实验记录，先从M0–M2完成环境、数据协议与可行性门槛；不要直接大规模训练。建议命令尚不存在，应先实现与测试。保留负例、错误、资源账目，不把计划或旧测试当作新机已验证结果。

## 仓库边界

- 仅文档交接，不表示全部旧资产已经迁移。
- 不公开未发表研究，不包含访问token、密码、私钥或外部账号授权。
- 旧路径只作历史证据定位，不能作为新机运行依赖。
- 新实验代码、权重和数据请在新机的独立研究目录中开发，依主文档另行版本管理。
