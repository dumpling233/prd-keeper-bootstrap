# 模块索引

当前模块结构基于仓库 README、根 `SKILL.md`、`routing.yaml`、`package.json`、`bin/prd-keeper.js`、`scripts/init_prd_keeper.py` 和 `templates/` 回填。后续新增能力时，应优先补齐对应模块 PRD，再修改实现。

既有项目接入治理时，不要求一次性补齐所有模块；后续每次任务应优先补齐本次涉及模块的 Baseline PRD，并把新增模块文档链接回本索引。

## 当前模块列表

- [Bootstrap 安装器](bootstrap-installer.md)：`package.json`、`bin/prd-keeper.js`、`scripts/init_prd_keeper.py`、`templates/`、`assets/`、根 `SKILL.md`、根 `routing.yaml` 和 README，负责把治理结构安装到目标项目，并提供 npm 命令包装入口与外部展示资产。
- [PRD Keeper 治理](prd-keeper.md)：`.agent/skills/prd-keeper/`、`AGENTS.md`、`CODEX.md`、`CLAUDE.md` 和 `docs/prd/`，定义 AI 开发与 PRD 维护流程。

## 待补充模块

- 暂无后端服务模块。
- 暂无前端界面模块。
- 后续如果实现 `scan`、`upgrade`、`--dry-run` 或配置化初始化，应补充独立模块文档或扩展 Bootstrap 安装器模块文档。

## 模块文档规则

模块文档应聚焦当前行为、业务规则、接口契约、数据字段、权限规则和边界情况，不记录历史过程。历史变更统一写入 `docs/prd/prd_log/YYYYMMDD-{git-user}.md`。
