# 产品概览

## 产品定位

`prd-keeper-bootstrap` 是面向 AI 辅助软件研发的项目级治理初始化工具。它通过 npm 命令包装器或离线 Python 脚本，把 PRD-first、可追溯、可审计的 AI 研发工作流安装到任意目标项目中。

它的核心价值不是生成业务代码，而是让项目获得稳定的 AI 入口、项目本地治理 Skill、分层 PRD、变更日志和结构校验能力。

## 核心场景

- 新项目从第一天开始建立 PRD-first AI 研发治理结构。
- 已有项目补装统一 Agent 入口、项目本地 `prd-keeper` Skill、PRD 模板和日志目录。
- 使用者通过 `npm install -g prd-keeper-bootstrap` 或 `npx prd-keeper-bootstrap init ...` 获取统一 `prd-keeper init` 命令入口。
- 团队希望让 Codex、Claude Code 或通用 Agent 进入项目后遵守同一套开发前后治理规则。
- 既有项目在后续任务中逐步回填 Baseline PRD，而不是在 bootstrap 安装阶段由脚本猜测业务事实。
- 项目维护者希望用仓库文件保存 AI 开发规则、需求上下文、架构说明和变更记录。

## 关键业务规则

- PRD 只描述当前真实行为，不记录愿望、计划或未经确认的猜测。
- 历史决策和变更过程写入 `docs/prd/prd_log/YYYYMMDD-{git-user}.md`，不写入模块当前行为文档。
- Bootstrap 默认不覆盖已有文件；只有传入 `--force` 时才覆盖模板目标文件。
- npm 入口只负责安装分发、命令注册、参数分发和 Python 解释器探测；真实初始化逻辑仍由 `scripts/init_prd_keeper.py` 执行。
- 通过 npm 入口运行时要求 Node.js >= 18 和 Python >= 3.9；可用 `PRD_KEEPER_PYTHON` 指定 Python 可执行文件。
- `package.json` 当前本地版本为 `0.1.1`，用于准备包含 README/logo 与 GitHub 元数据的下一次补丁发布；npm registry 在正式发布前仍以已发布版本为准。
- `package.json` 声明 GitHub 仓库、README 首页和 Issues 地址，供 npm 包页面展示源码、主页和问题反馈入口。
- Bootstrap 安装阶段不调用 AI，不联网，不自动分析目标项目业务。
- 对已有项目，生成后的 `prd-keeper` 规则会在后续具体任务中按相关范围逐步回填 Baseline PRD。
- 日志文件名中的 `{git-user}` 必须来自目标项目的 Git 配置，避免多人写入同一个日期日志文件。
- 入口文件保持薄壳，详细治理规则放在项目本地 `.agent/skills/prd-keeper/` 中。
- GitHub 首页 README 面向外部使用者，当前包含居中品牌 logo、npm/version/download/license/Node/Python badges、快捷导航、安装入口、能力边界、使用说明和许可证；内部 Roadmap、发布账号/scope、治理待确认事项和任务过程应沉淀在 `docs/prd/` 与 `docs/prd/prd_log/` 中。

## 非目标/边界

- 不提供前端页面、后端服务、数据库、网络 API 或 IDE 插件。
- 不生成目标项目业务代码。
- 不在安装时生成完整可信的业务 PRD。
- 不替代开发者对真实业务事实、许可证策略、团队流程和发布策略的确认。

## 当前已知风险

- npm 包已作为未加 scope 的公开包 `prd-keeper-bootstrap@0.1.0` 发布，`latest` 当前指向 `0.1.0`；仓库本地 `package.json` 已准备 `0.1.1`，正式发布前 npm 页面不会自动展示本地 README/logo 更新。后续如需迁移到 scoped package，需要另行规划包名和兼容策略。
- Windows 上 `python` 可能解析到 WindowsApps 占位入口；npm 包装器会优先尝试 `py -3`，也可通过 `PRD_KEEPER_PYTHON` 指定真实 Python 解释器。
- `scan`、`upgrade`、`--dry-run`、配置化初始化和 CI 校验属于内部 Roadmap/待确认方向，当前版本主要提供统一 `init` 能力；这些内容不作为 GitHub 首页 README 的主要内容。
