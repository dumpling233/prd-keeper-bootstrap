# 架构说明

## 系统结构

`prd-keeper-bootstrap` 是一个以文件模板、Python 标准库脚本和 Node.js npm 包装器为核心的离线 CLI 工具。仓库本身不包含常驻服务、前端应用或数据库。

- 前端：无前端界面。
- 后端：无后端服务；核心初始化逻辑是本地命令行脚本 `scripts/init_prd_keeper.py`，npm 入口 `bin/prd-keeper.js` 只负责命令包装和转发。
- 数据层：无数据库；所有输出均为目标项目中的仓库文件。
- 外部服务：初始化过程不依赖外部服务；脚本仅可选读取目标项目的 Git 配置。
- 部署方式：可以作为 npm 包安装、通过 npx 临时运行，也可以作为 Git 仓库或本地目录使用。

## 主要目录到产品模块的映射

- `.agent/skills/prd-keeper/`：项目级“以 PRD 为先”的开发 Skill，负责规则、路由、工作流、参考信息和校验。
- `docs/prd/`：PRD 总入口、产品概览、架构说明、模块索引、模块文档和独立 PRD 日志。
- `AGENTS.md`：通用 Agent 薄入口，指向 `prd-keeper` 和 `docs/prd/README.md`。
- `CODEX.md`：Codex 薄入口，指向 `prd-keeper` 和 `docs/prd/README.md`。
- `CLAUDE.md`：Claude 薄入口，指向 `prd-keeper` 和 `docs/prd/README.md`。
- `scripts/init_prd_keeper.py`：Bootstrap 安装器的主要源码，负责模板复制、变量渲染、日志创建和跳过已有文件。
- `bin/prd-keeper.js`：npm 命令包装器，提供 `prd-keeper init`、`--help` 和 `--version`，探测 Python >= 3.9 后转发到 `scripts/init_prd_keeper.py`。
- `package.json`：npm 包元数据，当前本地版本为 `0.1.1`，声明 `prd-keeper` 和 `prd-keeper-bootstrap` 两个 bin 命令、Node.js 版本要求、包含 `assets/` 的发布文件集合、GitHub repository/homepage/bugs 元数据和许可证。
- `assets/prd-keeper-logo.svg`：根 README 使用的外部展示 logo 资产，随 npm 包发布文件集合分发。
- `templates/`：安装到目标项目的文件模板，包括入口文件、项目本地 Skill、PRD 模板、工作流、规则、参考文档和脚本。
- `SKILL.md`：当前仓库作为 Codex Skill 被使用时的 bootstrap 入口。
- `routing.yaml`：当前仓库的 bootstrap 路由描述。
- 配置目录：当前没有独立配置目录。
- 测试目录：当前没有独立测试目录；结构验证依赖生成到目标项目的 `check_prd_keeper.py`。

## 关键数据流

1. 用户通过 `prd-keeper init`、`npx prd-keeper-bootstrap init` 或 `python scripts/init_prd_keeper.py` 指定目标目录和项目名称。
2. 如果使用 npm 入口，`bin/prd-keeper.js` 解析命令，探测 `PRD_KEEPER_PYTHON`、Windows `py -3`、`python` 或 `python3` 中可用的 Python >= 3.9。
3. npm 包装器将参数转发给 `scripts/init_prd_keeper.py`。
4. `scripts/init_prd_keeper.py` 读取目标项目 Git 配置，计算作者名和安全文件名片段。
5. 脚本递归读取 `templates/` 下的模板文件。
6. 脚本渲染模板变量，并将 `.tpl` 文件写入目标项目对应路径。
7. 如果目标文件已存在且未传入 `--force`，脚本跳过该文件。
8. 脚本创建或追加目标项目 `docs/prd/prd_log/YYYYMMDD-{git-user}.md` 初始化日志。
9. 用户在目标项目中运行生成的 `check_prd_keeper.py` 校验治理结构。

## 权限、配置、环境变量和第三方服务边界

- 权限/鉴权：不涉及账号、登录、角色或鉴权流程。
- 配置项：当前通过命令行参数 `init`、`--target`、`--project-name` 和 `--force` 控制。
- 环境变量：Python 脚本自身没有必需环境变量；npm 包装器可选读取 `PRD_KEEPER_PYTHON` 指定 Python 可执行文件。
- 第三方服务：初始化运行无必需第三方服务；Git 仅用于读取本地 `user.name` 或 `user.email`。发布 npm 包时需要维护者使用 npm registry 账号手动发布。
- 日志：安装日志写入目标项目 `docs/prd/prd_log/YYYYMMDD-{git-user}.md`。

## AI 修改代码时需要注意的架构约束

- 非平凡变更前必须读取 `docs/prd/README.md`、`docs/prd/product-overview.md`、`docs/prd/modules/README.md`、`docs/prd/architecture.md`、`.agent/skills/prd-keeper/references/project-map.md`、`.agent/skills/prd-keeper/references/gotchas.md` 和最近相关日志。
- 新增接口、页面、数据结构、权限、配置项或外部服务时，必须同步更新本文件和相关模块文档。
- 如果代码与 PRD 冲突，以当前代码和用户最新明确需求为准，完成修改后同步 PRD。
