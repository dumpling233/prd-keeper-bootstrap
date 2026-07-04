# 架构说明

## 系统结构

既有项目接入治理时，本文件应在后续任务中随着代码阅读逐步回填。只记录已由代码、配置、运行脚本、部署文件或用户说明确认的结构；无法确认的内容保留为 `待确认`。

- 前端：待确认。
- 后端：待确认。
- 数据层：待确认。
- 外部服务：待确认。
- 部署方式：待确认。

## 主要目录到产品模块的映射

- `.agent/skills/prd-keeper/`：项目级“以 PRD 为先”的开发 Skill，负责规则、路由、工作流、参考信息和校验。
- `docs/prd/`：PRD 总入口、产品概览、架构说明、模块索引、模块文档和独立 PRD 日志。
- `AGENTS.md`：通用 Agent 薄入口，指向 `prd-keeper` 和 `docs/prd/README.md`。
- `CODEX.md`：Codex 薄入口，指向 `prd-keeper` 和 `docs/prd/README.md`。
- `CLAUDE.md`：Claude 薄入口，指向 `prd-keeper` 和 `docs/prd/README.md`。
- 源码目录：待确认。
- 配置目录：待确认。
- 测试目录：待确认。

## 关键数据流

- 待确认。

## 权限、配置、环境变量和第三方服务边界

- 权限/鉴权：待确认。
- 配置项：待确认。
- 环境变量：待确认。
- 第三方服务：待确认。
- 日志：待确认。

## AI 修改代码时需要注意的架构约束

- 非平凡变更前必须读取 `docs/prd/README.md`、`docs/prd/product-overview.md`、`docs/prd/modules/README.md`、`docs/prd/architecture.md`、`.agent/skills/prd-keeper/references/project-map.md`、`.agent/skills/prd-keeper/references/gotchas.md` 和最近相关日志。
- 新增接口、页面、数据结构、权限、配置项或外部服务时，必须同步更新本文件和相关模块文档。
- 如果代码与 PRD 冲突，以当前代码和用户最新明确需求为准，完成修改后同步 PRD。
