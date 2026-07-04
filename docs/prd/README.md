# prd-keeper-bootstrap PRD 总入口

AI 在进行非平凡代码变更前必须先使用 `$prd-keeper`，阅读本文件，再继续阅读相关模块文档、架构文档和最近相关 PRD 日志。修改代码时必须结合 PRD 与现有代码；修改完成后，如果产品行为或工程约束发生变化，必须更新对应 PRD，并在 `docs/prd/prd_log/YYYYMMDD-{git-user}.md` 创建或追加日志；`{git-user}` 必须读取 `git config user.name`。

## 项目一句话说明

`prd-keeper-bootstrap` 是一个离线、确定性的 PRD-first AI 研发治理初始化器，通过 npm 命令包装器或 Python 标准库脚本，把统一 Agent 入口、项目本地 `prd-keeper` Skill、分层 PRD、PRD 日志和校验脚本安装到目标项目中。

## 既有项目渐进式治理接管

如果本项目是在已有代码基础上接入 `prd-keeper`，本文件中的 `待确认` 项不要求一次性全部补完。后续每次非平凡任务开始时，AI 应先检查本次任务相关范围的 PRD 是否足以描述当前真实行为；若不足，应先结合代码、配置、README、接口、页面、数据结构和用户说明回填相关 Baseline PRD，再继续开发。

## 当前产品目标

- 为新项目或已有项目安装轻量级、项目内、可审计的 AI 研发治理结构。
- 让后续 AI 开发先读取 PRD 和项目内治理规则，再修改代码，并在任务结束时同步 PRD 与日志。
- 保持 bootstrap 阶段离线、确定、可复现，不在安装时调用大模型或猜测目标项目业务事实。

## 核心用户/角色

- 产品使用者：希望把项目纳入 PRD-first AI 研发治理的个人开发者或团队。
- 项目维护者：负责在目标项目中运行初始化命令、确认真实业务事实、维护治理模板。
- AI 开发代理：通过 `AGENTS.md`、`CODEX.md` 或 `CLAUDE.md` 进入 `$prd-keeper` 工作流，修改代码前必须阅读 PRD，修改后必须更新受影响文档并创建或追加当前 Git 用户当天的 PRD 日志。
- 目标项目成员：在被初始化的项目中按生成的入口文件和项目本地 Skill 继续开发。

## 主流程入口

- npm 命令入口：`prd-keeper init --target <target-project> --project-name <project-name> [--force]`。
- npx 命令入口：`npx prd-keeper-bootstrap init --target <target-project> --project-name <project-name> [--force]`。
- Python 源码入口：`python scripts/init_prd_keeper.py --target <target-project> --project-name <project-name> [--force]`。
- GitHub 源码入口：`https://github.com/dumpling233/prd-keeper-bootstrap`。
- npm 包装器入口：`bin/prd-keeper.js`，负责解析 `init`、`--help`、`--version`，定位 Python >= 3.9 并转发到 `scripts/init_prd_keeper.py`。
- GitHub/npm 展示入口：根目录 `README.md` 和 `assets/prd-keeper-logo.svg`，面向外部使用者展示品牌、安装入口、能力边界和使用说明。
- 本项目作为 Codex Skill 的入口：根目录 `SKILL.md`。
- 生成到目标项目的治理入口：`AGENTS.md`、`CODEX.md`、`CLAUDE.md` 和 `.agent/skills/prd-keeper/SKILL.md`。
- 后端入口：不适用；本项目不是后端服务。
- 前端入口：不适用；本项目没有前端界面。
- API 入口：不适用；本项目不提供网络 API。

## 模块索引

- [模块索引](modules/README.md)
- [Bootstrap 安装器](modules/bootstrap-installer.md)
- [PRD Keeper 治理](modules/prd-keeper.md)

## 架构文档

- [架构说明](architecture.md)

## 产品概览

- [产品概览](product-overview.md)

## 最近 PRD 日志

- 初始化日志位于 [prd_log](prd_log)。

## 待确认

以下事项会在后续受控任务中逐步确认。不要根据模板、目录名或项目名编造；优先消除本次任务相关范围内影响判断和实现的未知项。

- 是否继续同时维护 `AGENTS.md`、`CODEX.md` 和 `CLAUDE.md` 三个入口，还是按目标用户群收敛入口文件。
- Roadmap 中 `scan`、`upgrade`、`--dry-run`、配置化初始化和 CI 校验的优先级。
