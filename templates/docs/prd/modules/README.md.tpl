# 模块索引

当前模块结构待确认。初始化后应根据真实代码目录和产品边界维护模块文档。

既有项目接入治理时，不要求一次性补齐所有模块；后续每次任务应优先补齐本次涉及模块的 Baseline PRD，并把新增模块文档链接回本索引。

## 当前模块列表

- [PRD Keeper 治理](prd-keeper.md)：`.agent/skills/prd-keeper/`、`AGENTS.md`、`CODEX.md`、`CLAUDE.md` 和 `docs/prd/`，定义 AI 开发与 PRD 维护流程。

## 待补充模块

- 后端模块：待确认。
- 前端模块：待确认。
- 数据/脚本/任务模块：待确认。

## 模块文档规则

模块文档应聚焦当前行为、业务规则、接口契约、数据字段、权限规则和边界情况，不记录历史过程。历史变更统一写入 `docs/prd/prd_log/YYYYMMDD-{git-user}.md`。
