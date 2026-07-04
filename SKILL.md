---
name: prd-keeper-bootstrap
description: "初始化或升级通用 PRD-first 可审计 AI 研发闭环。Use when starting a new project, installing PRD Keeper into an existing project, creating AGENTS/CODEX/CLAUDE entries, generating docs/prd templates, creating project-local .agent/skills/prd-keeper, or migrating a project to auditable PRD-first AI development."
---

# PRD Keeper Bootstrap

`prd-keeper-bootstrap` 是通用安装器 Skill，用于把“PRD-first 可审计 AI 研发闭环”安装到任意项目中。它不替代项目内的 `prd-keeper`；它负责生成项目内 `prd-keeper`、PRD 模板、入口文件、日志脚本和校验脚本。

## Always Read

- `routing.yaml`
- `README.md`
- `scripts/init_prd_keeper.py`

## 核心交付

- 根入口文件：`AGENTS.md`、`CODEX.md`、`CLAUDE.md`
- 项目内 Skill：`.agent/skills/prd-keeper/`
- 分层 PRD：`docs/prd/`
- 既有项目渐进式治理接管规则：PRD 缺失、待确认或与代码不一致时，生成的 `prd-keeper` 会要求先补齐相关范围 Baseline PRD
- 可审计日志目录：`docs/prd/prd_log/`
- 日志生成脚本：`.agent/skills/prd-keeper/scripts/new_prd_log.py`
- 结构校验脚本：`.agent/skills/prd-keeper/scripts/check_prd_keeper.py`

## 使用纪律

- 初始化前先确认目标目录，避免把模板写到错误项目。
- 对已有项目默认不覆盖文件；只有用户明确同意或传入 `--force` 才覆盖。
- 初始化后由项目内 `.agent/skills/prd-keeper/` 接管日常开发治理。
- 项目事实必须在初始化后由 AI 读取真实代码、配置和用户说明再填充，不从模板猜测。
- 新项目初始化完成后，应立即运行生成出的 `check_prd_keeper.py`。

## 推荐命令

```powershell
python D:\work\prd-keeper-bootstrap\scripts\init_prd_keeper.py --target D:\path\to\project --project-name your-project
```

当前目录初始化：

```powershell
python D:\work\prd-keeper-bootstrap\scripts\init_prd_keeper.py --target . --project-name your-project
```
