# 项目地图

本文件记录当前项目结构，用于路由和 PRD 维护。初始化后需要结合真实代码、配置和用户说明填充。

既有项目接入治理时，本文件可以随后续任务逐步完善；优先补齐本次任务相关的路径、命令、模块和约束。

## 项目

- 项目名称：`prd-keeper-bootstrap`
- 项目路径：`D:\self-work\prd-keeper-bootstrap`
- 技术栈：Python 标准库脚本、Markdown/YAML 模板、Git 本地配置。
- 业务领域：PRD-first 可审计 AI 辅助软件研发治理初始化。

## 已确认结构

- `scripts/init_prd_keeper.py`：离线初始化脚本，负责复制模板、渲染变量、跳过或覆盖目标文件、创建 PRD 初始化日志。
- `templates/`：目标项目治理结构模板。
- `SKILL.md`：当前仓库作为 bootstrap Skill 的入口。
- `routing.yaml`：当前仓库的 bootstrap 路由。
- `.agent/skills/prd-keeper/`：项目级 PRD-first 开发 Skill。
- `docs/prd/`：PRD 总入口、产品概览、架构、模块索引、模块文档和独立 PRD 日志。
- `AGENTS.md`、`CODEX.md`、`CLAUDE.md`：AI 入口文件。

## 待确认结构

- 构建命令：当前无构建步骤。
- 测试命令：当前无独立测试套件；治理结构校验命令为 `python .agent\skills\prd-keeper\scripts\check_prd_keeper.py`。
- 配置目录：当前无独立配置目录。
- 部署方式：当前作为 Git 仓库或本地目录使用。

## 当前 PRD 文件

- `docs/prd/README.md`
- `docs/prd/product-overview.md`
- `docs/prd/architecture.md`
- `docs/prd/modules/README.md`
- `docs/prd/modules/bootstrap-installer.md`
- `docs/prd/modules/prd-keeper.md`
- `docs/prd/prd_log/`
