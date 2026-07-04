# Bootstrap 安装器模块

## 模块范围

Bootstrap 安装器模块由 `package.json`、`bin/prd-keeper.js`、`scripts/init_prd_keeper.py`、`templates/`、`assets/`、根目录 `SKILL.md`、根目录 `routing.yaml` 和项目 README 组成。它负责把 PRD Keeper 治理环境安装到用户指定的目标项目目录，并提供 npm 分发入口与外部展示资产。

## 当前入口

- npm 命令入口：`prd-keeper init --target <target-project> --project-name <project-name>`
- npx 命令入口：`npx prd-keeper-bootstrap init --target <target-project> --project-name <project-name>`
- Python 源码入口：`python scripts/init_prd_keeper.py --target <target-project> --project-name <project-name>`
- GitHub 源码入口：`https://github.com/dumpling233/prd-keeper-bootstrap`
- 覆盖模式：追加 `--force` 后覆盖已存在的模板目标文件。
- 当前项目自举命令：`prd-keeper init --target . --project-name prd-keeper-bootstrap`；源码开发场景也可使用 `python scripts/init_prd_keeper.py --target . --project-name prd-keeper-bootstrap`。

## 当前行为

- npm 包元数据在 `package.json` 中声明本地版本 `0.1.1`、GitHub repository/homepage/bugs 元数据、`prd-keeper` 和 `prd-keeper-bootstrap` 两个 bin 命令，发布文件包含 `bin/`、`assets/`、`scripts/`、`templates/`、README、LICENSE、根 `SKILL.md` 和根 `routing.yaml`。
- `bin/prd-keeper.js` 支持 `prd-keeper --help`、`prd-keeper --version`、`prd-keeper init ...`，如果第一个参数直接以 `-` 开头，会按 `init` 参数处理。
- npm 包装器要求 Node.js >= 18，并会探测 Python >= 3.9：优先使用 `PRD_KEEPER_PYTHON`，Windows 下随后尝试 `py -3`、`python`、`python3`，非 Windows 下尝试 `python3`、`python`。
- npm 包装器只负责命令解析、Python 探测和参数转发；真实安装行为由 `scripts/init_prd_keeper.py` 执行。
- Python 脚本要求 `--target` 指向一个已经存在的目录；如果目标不存在或不是目录，会直接退出。
- `--project-name` 省略时使用目标目录名。
- 脚本从 `templates/` 递归读取模板文件，去掉目标文件名末尾的 `.tpl`，再写入目标项目对应路径。
- 文本模板会替换 `{{PROJECT_NAME}}`、`{{PROJECT_SLUG}}`、`{{DATE_YYYYMMDD}}`、`{{DATE_ISO}}`、`{{GIT_USER}}` 和 `{{GIT_USER_SLUG}}`。
- `GIT_USER` 优先来自目标项目中的 `git config user.name`，其次来自 `git config user.email`，最后回退为 `unknown`。
- 默认不覆盖目标项目已有文件；存在冲突时记录为 skipped。
- 初始化完成后会确保目标项目存在 `docs/prd/prd_log/`，并创建或追加 `YYYYMMDD-{git-user}.md` 初始化日志。
- 脚本不调用大模型、不访问网络、不分析目标项目业务代码，只做确定性的文件安装。
- 根 README 面向外部使用者展示品牌 logo、npm badges、快捷导航、安装、初始化、校验和日常使用；内部 Roadmap、发布账号/scope、治理待确认事项和任务过程不放在 GitHub 首页 README，保留在 PRD 与日志中。

## 生成内容

- 根入口文件：`AGENTS.md`、`CODEX.md`、`CLAUDE.md`
- 项目本地 Skill：`.agent/skills/prd-keeper/`
- PRD 文档体系：`docs/prd/`
- PRD 日志目录：`docs/prd/prd_log/`
- 日志生成脚本：`.agent/skills/prd-keeper/scripts/new_prd_log.py`
- 结构校验脚本：`.agent/skills/prd-keeper/scripts/check_prd_keeper.py`

## 边界

- 不生成前端、后端、数据库或业务功能代码。
- npm 入口不移除 Python 前置要求；它是当前 Python 初始化器的分发和命令包装层。
- 不在安装阶段自动生成可信业务 PRD。
- 不负责判断目标项目真实产品目标、接口契约、权限规则或数据模型。
- 对已有项目接入治理时，只安装治理结构；目标项目事实由后续受治理的 AI 协作逐步回填。

## 已知风险

- Windows 环境中 `python` 可能先解析到 WindowsApps 占位入口，导致命令无法运行；需要确认真实 Python 路径在 PATH 中优先于 WindowsApps，或直接调用真实解释器路径。
- npm 包已作为公开包 `prd-keeper-bootstrap@0.1.0` 发布，`latest` 当前指向 `0.1.0`；仓库本地 `package.json` 已准备 `0.1.1`，正式发布前 npm 页面不会自动展示本地 README/logo 更新。后续如需改为 scoped package，需要另行规划迁移与兼容策略。
