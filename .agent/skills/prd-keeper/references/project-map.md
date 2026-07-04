# 项目地图

本文件记录当前项目结构，用于路由和 PRD 维护。初始化后需要结合真实代码、配置和用户说明填充。

既有项目接入治理时，本文件可以随后续任务逐步完善；优先补齐本次任务相关的路径、命令、模块和约束。

## 项目

- 项目名称：`prd-keeper-bootstrap`
- 项目路径：`D:\self-work\prd-keeper-bootstrap`
- 技术栈：Node.js npm 命令包装器、Python 标准库脚本、Markdown/YAML 模板、Git 本地配置。
- 业务领域：PRD-first 可审计 AI 辅助软件研发治理初始化。

## 已确认结构

- `package.json`：npm 包元数据，当前本地版本为 `0.1.1`，声明 `prd-keeper` 与 `prd-keeper-bootstrap` bin 命令、Node.js 版本要求、GitHub repository/homepage/bugs、发布文件集合和许可证。
- `assets/prd-keeper-logo.svg`：GitHub/npm README 顶部展示 logo，纳入 npm 发布文件集合。
- `bin/prd-keeper.js`：npm 命令包装器，解析 `init`、`--help`、`--version`，探测 Python >= 3.9 后转发到 `scripts/init_prd_keeper.py`。
- `scripts/init_prd_keeper.py`：离线初始化脚本，负责复制模板、渲染变量、跳过或覆盖目标文件、创建 PRD 初始化日志。
- `templates/`：目标项目治理结构模板。
- `SKILL.md`：当前仓库作为 bootstrap Skill 的入口。
- `routing.yaml`：当前仓库的 bootstrap 路由。
- `.agent/skills/prd-keeper/`：项目级 PRD-first 开发 Skill。
- `docs/prd/`：PRD 总入口、产品概览、架构、模块索引、模块文档和独立 PRD 日志。
- `AGENTS.md`、`CODEX.md`、`CLAUDE.md`：AI 入口文件。

## 待确认结构

- 构建命令：当前无构建步骤；发布前可运行 `npm run pack:check` 预览 npm 包内容。
- 测试命令：当前无独立测试套件；npm CLI 帮助命令为 `npm run cli:help`，治理结构校验命令为 `python .agent\skills\prd-keeper\scripts\check_prd_keeper.py`。
- 配置目录：当前无独立配置目录。
- 部署方式：当前可作为 npm 包、Git 仓库或本地目录使用。

## 当前 PRD 文件

- `docs/prd/README.md`
- `docs/prd/product-overview.md`
- `docs/prd/architecture.md`
- `docs/prd/modules/README.md`
- `docs/prd/modules/bootstrap-installer.md`
- `docs/prd/modules/prd-keeper.md`
- `docs/prd/prd_log/`
