# PRD Keeper Bootstrap

**PRD Keeper Bootstrap** 是一个用于初始化 **PRD-first 可审计 AI 辅助研发闭环** 的项目治理脚手架。

它的核心职责不是生成业务代码，而是把一套项目级 AI 研发治理结构安装到目标目录中，使项目具备统一的 Agent 入口、项目本地 Skill、分层 PRD、变更日志和校验脚本。

一句话定义：

> **PRD Keeper Bootstrap 是面向 AI 辅助软件研发的项目级治理初始化工具，用于把任意目标项目初始化为 PRD-first、可追溯、可审计的 AI 研发工作区。**

初始化完成后的目标项目可以称为：

> **PRD Keeper Workspace**，即一个被 PRD Keeper 治理规则接管的项目工作区。

---

## 先回答几个关键问题

| 问题 | 答案 |
| --- | --- |
| 它是业务代码脚手架吗？ | 不是。它不生成前端、后端或业务代码，只安装 AI 研发治理环境。 |
| 它能用于新项目吗？ | 能。新项目可以从第一天开始用 PRD-first 方式沉淀产品形态、架构、模块和变更历史。 |
| 它能用于已有项目吗？ | 能。它会给已有项目补装治理结构，不重写业务代码，已有文件默认跳过。 |
| 已有项目接入后是不是只记录未来变更？ | 不是。生成的 Agent/Skill 会在后续任务中发现 PRD 缺失、待确认或与代码不一致时，逐步回填相关范围的 Baseline PRD。 |
| 脚本会在安装时自动理解整个项目吗？ | 不会。脚本不接入大模型，只做确定性安装。项目理解发生在后续 AI 受治理协作过程中。 |
| 安装后用户还要每次手动说一大段治理提示吗？ | 理想情况下不需要。只要 AI 从生成的 `AGENTS.md`、`CODEX.md` 或 `CLAUDE.md` 进入，治理规则会由项目本地 `prd-keeper` Skill 触发。 |
| 是否完全无感？ | 接近无感，但有前提：你使用的 AI 工具必须会读取并遵守项目入口文件或你明确要求它“从 AGENTS.md/CODEX.md/CLAUDE.md 进入”。 |

最重要的使用心智是：

> **Bootstrap 只负责安装治理系统；生成出来的项目级 Agent/Skill 负责把后续 AI 对话纳入 PRD-first 可审计闭环。**

---

## 当前能力边界

当前版本提供的是一个统一的 `init` 能力：

> **init = 在目标项目中安装 PRD Keeper 治理环境。**

这里的“初始化”指的是初始化治理环境，而不是只能初始化一个空白新项目。

| 目标目录类型 | 当前是否支持 | 当前工具做什么 |
| --- | --- | --- |
| 新项目 / 空目录 | 支持 | 安装治理结构，生成 PRD 模板、Agent 入口、日志目录和校验脚本 |
| 既有项目 / 已有代码项目 | 支持 | 在不重写业务代码的前提下补装治理结构；已有文件默认跳过 |
| 已接入 PRD Keeper 的项目 | 部分支持 | 可重复运行并跳过已有文件；更完整的升级能力属于后续 Roadmap |

当前版本不会在脚本执行过程中调用 AI 大模型，也不会自动理解项目业务。因此它不会自动生成可信的产品目标、业务规则、页面说明、接口语义或数据模型 PRD。

对既有项目来说，Bootstrap 负责安装治理骨架，并把“渐进式治理接管”规则写入生成的项目级 Agent 和 `prd-keeper` Skill。真实业务事实不会在脚本执行时被自动生成，而会在后续 AI 协作过程中，基于现有代码、配置、README、接口、数据库、页面和开发者确认逐步回填到 `docs/prd/` 中。

---

## 它解决什么问题

在 AI 辅助开发中，真正的问题通常不是“AI 写不了代码”，而是 AI 写完代码之后，项目是否还能长期被理解、维护、审计和迭代。

| 常见问题 | 典型表现 | PRD Keeper 的处理方式 |
| --- | --- | --- |
| 需求漂移 | AI 按临时指令直接改代码，项目目标逐渐失焦 | 要求开发前回到 PRD、架构和模块文档确认依据 |
| 文档失真 | 代码已经变化，PRD、接口说明、模块说明没有同步 | 行为、接口、页面、数据、权限或业务规则变化后同步 PRD |
| 过程不可审计 | 不知道一次变更为什么发生、依据是什么、影响了哪里 | 通过标准化 PRD 变更日志记录过程 |
| Agent 行为不一致 | 不同 AI 工具进入项目后遵循不同规则 | 生成统一入口和项目本地 `prd-keeper` Skill |
| 项目知识断层 | 后续维护者难以理解历史决策和业务边界 | 用分层 PRD、架构文档、模块文档和日志保存上下文 |
| 缺少闭环 | 需求、实现、验证、记录之间没有强制连接 | 用流程规则和校验脚本形成研发闭环 |

---

## 它到底是什么

| 维度 | 说明 |
| --- | --- |
| 项目名称 | **PRD Keeper Bootstrap** |
| 中文名称 | **PRD Keeper 项目治理初始化器** |
| 工具类型 | AI 研发治理脚手架 / Agent 工作流初始化器 / PRD-first SDLC Governance Bootstrap |
| 当前核心能力 | 通过统一 `init` 命令向目标项目安装 PRD Keeper 治理环境 |
| 目标目录 | 可以是新项目，也可以是已有项目 |
| 主要产物 | Agent 入口、项目本地 Skill、PRD 文档体系、变更日志、校验脚本 |
| 不是什么 | 不是业务代码生成器，不是前后端项目模板，不是自动 PRD 生成器，不是 IDE 插件 |

---

## 命名体系

| 名称 | 含义 |
| --- | --- |
| **PRD Keeper** | 整套 PRD-first AI 研发治理方案的总称 |
| **PRD Keeper Bootstrap** | 用于把治理方案安装到项目中的初始化工具 |
| **prd-keeper Skill** | 生成到目标项目内的 AI Agent 行为规则和工作流 |
| **PRD Keeper Workspace** | 初始化完成后的受治理项目工作区 |
| **PRD-first Auditable AI-assisted SDLC Governance** | 这套方法论的英文专业描述 |

中文专业描述：

> **PRD-first 可审计 AI 辅助软件研发生命周期治理**

---

## 生成内容

执行初始化后，目标项目会生成类似结构：

```text
your-project/
├─ AGENTS.md
├─ CODEX.md
├─ CLAUDE.md
├─ .agent/
│  └─ skills/
│     └─ prd-keeper/
│        ├─ SKILL.md
│        ├─ routing.yaml
│        ├─ rules/
│        ├─ workflows/
│        ├─ references/
│        └─ scripts/
└─ docs/
   └─ prd/
      ├─ README.md
      ├─ product-overview.md
      ├─ architecture.md
      ├─ modules/
      └─ prd_log/
```

| 组件 | 作用 |
| --- | --- |
| `AGENTS.md` | 通用 AI Agent 入口，要求 AI 先进入治理流程再开发 |
| `CODEX.md` | 面向 Codex 类工具的入口适配文件 |
| `CLAUDE.md` | 面向 Claude Code 类工具的入口适配文件 |
| `.agent/skills/prd-keeper/` | 项目本地治理 Skill，定义 AI 如何读 PRD、改代码、写日志、做收尾，并在 PRD 缺失或不一致时触发相关范围的 Baseline PRD 回填 |
| `docs/prd/` | PRD-first 文档体系，保存产品、架构、模块和规则说明 |
| `docs/prd/prd_log/` | 研发过程日志，用于记录重要变更 |
| `check_prd_keeper.py` | 校验治理结构是否完整 |
| `new_prd_log.py` | 快速创建标准 PRD 变更日志 |

---

## 快速开始

### 1. 获取工具

```bash
git clone https://github.com/your-name/prd-keeper-bootstrap.git
cd prd-keeper-bootstrap
```

如果你还没有创建 GitHub 仓库，也可以先在本地直接使用当前目录中的脚本。

### 2. 初始化治理环境

目标目录可以是新项目，也可以是已有项目：

```bash
python scripts/init_prd_keeper.py --target /path/to/your-project --project-name your-project
```

Windows 示例：

```powershell
python D:\work\prd-keeper-bootstrap\scripts\init_prd_keeper.py --target D:\work\your-project --project-name your-project
```

参数说明：

| 参数 | 含义 |
| --- | --- |
| `--target` | 要安装治理结构的目标项目目录；可以是空项目，也可以是已有项目 |
| `--project-name` | 目标项目显示名称，用于模板标题和日志说明；不代表只能用于新项目 |
| `--force` | 覆盖已存在的模板文件；默认不覆盖 |

默认情况下，初始化脚本不会覆盖目标项目中已经存在的文件。对已有项目接入治理时，建议先不使用 `--force`。

如果确认需要覆盖模板文件，可以使用：

```bash
python scripts/init_prd_keeper.py --target /path/to/your-project --project-name your-project --force
```

### 3. 在目标项目中执行校验

```bash
python .agent/skills/prd-keeper/scripts/check_prd_keeper.py
```

校验通过时会看到类似输出：

```text
prd-keeper validation passed
```

### 4. 创建一次 PRD 变更日志

```bash
python .agent/skills/prd-keeper/scripts/new_prd_log.py --title "新增用户登录能力"
```

### 5. 日常使用：继续正常提需求

初始化完成后，用户不需要每次手动复述完整治理流程。日常可以继续像以前一样提出开发需求，例如：

```text
帮我新增用户登录能力。
```

关键前提是：AI 工具需要从生成的项目入口进入治理流程。

| 使用方式 | 推荐提示 |
| --- | --- |
| 通用 Agent | `从 AGENTS.md 进入，按 prd-keeper 流程开发。` |
| Codex | `从 CODEX.md 进入，按 prd-keeper 流程开发。` |
| Claude Code | `从 CLAUDE.md 进入，按 prd-keeper 流程开发。` |

当 AI 进入 `prd-keeper` 后，后续流程由项目本地 Skill 约束：先读 PRD，再读相关代码；如果相关 PRD 缺失、仍为 `待确认` 或与代码现状不一致，先补齐本次任务相关范围的 Baseline PRD，再继续实现；完成后同步 PRD 和日志。

---

## 新项目与既有项目的后续差异

当前脚本对新项目和既有项目执行的是同一类确定性安装逻辑。差异不在脚本安装阶段，而在初始化后的治理节奏。

| 场景 | 初始化后的治理方式 |
| --- | --- |
| 新项目 | 从项目早期开始补充产品目标、架构设想、模块规划，并在每次开发中持续同步 PRD |
| 既有项目 | 生成的 Agent/Skill 会在后续任务中检查相关 PRD 是否缺失、仍为 `待确认` 或与代码不一致；若不足，先回填本次任务相关范围的 Baseline PRD，再继续实现 |

因此，既有项目接入后并不是只记录“接入之后的新变更”。它会通过后续受约束的 AI 对话，把原本散落在代码、配置、页面、接口和开发者经验中的项目事实逐步迁移到 `docs/prd/` 中。

用户可以像以前一样继续提出开发需求；只要 AI 从 `AGENTS.md`、`CODEX.md` 或 `CLAUDE.md` 进入，生成的 `prd-keeper` 规则就会在 PRD 缺失或不一致时触发相关范围的渐进式治理接管。

如果希望先做一次显式接管，也可以对 AI 说：

```text
从 AGENTS.md 进入，按 prd-keeper 流程接管当前项目。先不要改业务代码，请阅读 README、配置、目录结构和核心模块，回填 docs/prd/ 的 Baseline PRD，并记录本次接入日志。
```

这一步是可选的集中式基线回填任务；没有执行它，也不影响后续任务中的渐进式回填。

---

## 是否无感切换到治理模式

可以把使用体验理解为：**安装一次，后续由项目级 Agent/Skill 持续接管 AI 协作习惯。**

| 阶段 | 用户感知 | 实际发生的治理动作 |
| --- | --- | --- |
| 安装时 | 运行一次初始化命令 | 生成入口文件、项目本地 Skill、PRD 模板、日志目录和校验脚本 |
| 第一次让 AI 工作 | 确认 AI 从入口文件进入 | AI 读取 `AGENTS.md` / `CODEX.md` / `CLAUDE.md`，进入 `prd-keeper` |
| 后续正常开发 | 用户继续按原习惯提需求 | AI 自动按规则读 PRD、查代码、补 Baseline、改实现、同步文档、写日志 |
| PRD 不完整时 | 用户不需要专门判断 | AI 在相关任务范围内触发渐进式治理接管 |
| 任务结束时 | 用户收到结果 | AI 说明代码变化、PRD 更新、日志状态、验证结果和风险 |

这不是脚本在安装时“瞬间理解整个项目”，而是把理解项目的规则写进项目本身，让后续每次 AI 协作都帮助项目知识更完整、更可审计。

---

## 推荐研发闭环

PRD Keeper 推荐所有非平凡开发任务遵循以下闭环：

| 阶段 | 动作 | 目标 |
| --- | --- | --- |
| 1. 进入治理入口 | AI 先阅读 `AGENTS.md`、`CODEX.md` 或 `CLAUDE.md` | 统一 Agent 行为入口 |
| 2. 读取 Skill | AI 阅读 `.agent/skills/prd-keeper/SKILL.md` 和 `routing.yaml` | 获取项目内治理规则 |
| 3. 读取 PRD | 从 `docs/prd/README.md` 进入产品、架构和模块文档 | 明确需求依据 |
| 4. 检查基线 | 若相关 PRD 缺失、仍为 `待确认` 或与代码不一致，先补齐本次任务相关范围的 Baseline PRD | 渐进式接管既有项目 |
| 5. 确认影响范围 | 判断本次任务影响哪些模块、接口、页面、数据或权限 | 防止无边界修改 |
| 6. 修改实现 | 在理解 PRD 和现有代码后进行开发 | 完成代码变更 |
| 7. 同步文档 | 如果行为或规则变化，更新对应 PRD | 防止文档漂移 |
| 8. 写入日志 | 在 `docs/prd/prd_log/` 中记录背景、内容、影响和验证 | 留下可审计证据 |
| 9. 执行校验 | 运行校验脚本或项目测试 | 完成闭环收尾 |

---

## 职责边界

PRD Keeper Bootstrap 的设计原则是：**脚本负责确定性工作，AI Agent 和开发者负责语义理解与事实确认。**

| 工作内容 | 当前 Bootstrap 脚本 | AI Agent / 开发者 |
| --- | --- | --- |
| 安装治理目录结构 | 负责 | 不需要 |
| 生成 Agent 入口和 Skill 模板 | 负责 | 不需要 |
| 生成 PRD 模板和日志目录 | 负责 | 不需要 |
| 校验治理结构是否完整 | 负责 | 可辅助运行 |
| 判断真实产品目标 | 不负责 | 负责确认 |
| 梳理业务规则、页面、接口和数据模型 | 不负责 | 负责确认 |
| 生成可信 Baseline PRD | 安装时不自动生成 | 由生成的 `prd-keeper` 规则引导 AI Agent 逐步撰写，并由开发者确认 |

---

## 设计原则

| 原则 | 说明 |
| --- | --- |
| Unified Init | 当前使用统一 `init` 初始化治理环境，不强行区分空项目和已有项目 |
| Progressive Adoption | 既有项目接入后，通过生成的 Agent/Skill 在后续任务中逐步补齐项目事实 |
| PRD-first | 非平凡开发必须先回到 PRD、架构和模块文档确认依据 |
| Auditability | 重要变更必须留下可追溯记录 |
| Docs-as-Code | PRD、架构、模块说明和日志都作为仓库文件维护 |
| Agent-local Governance | 治理规则跟随项目本身，而不是只存在于某个聊天上下文中 |
| Minimal Business Assumption | Bootstrap 只安装治理结构，不猜测目标项目的真实业务 |
| Continuous Sync | 代码变化后，相关 PRD 和日志需要同步更新 |
| Tool Neutrality | 尽量兼容不同 AI 编程工具，而不是绑定单一 Agent |

---

## 适用场景

适合使用 PRD Keeper Bootstrap 的场景：

- 新项目希望从第一天开始具备 AI 研发治理结构
- 既有项目希望补装 PRD-first、可审计、可追溯的 AI 研发闭环
- 使用 AI 长期辅助开发的软件项目
- 希望规范 AI 编程行为的个人或团队
- 需要沉淀需求、架构、模块和变更历史的项目
- 需要让不同 AI 工具遵循统一开发规则的项目
- 希望把“AI 写代码”升级为“AI 参与受治理的软件工程”的团队

不太适合的场景：

- 一次性 Demo
- 不需要文档和维护的小实验
- 只想快速生成业务代码、不关心过程治理的项目
- 期望脚本在安装瞬间自动理解项目业务并直接生成准确 PRD 的场景
- 已经有完整内部 SDLC 平台且不希望引入项目内文档治理结构的团队

---

## 常见疑问

### 为什么当前只有统一 `init`，没有单独 `adopt`？

当前脚本的确定性能力是“安装治理环境”，这件事对新项目和既有项目是一样的：生成入口、Skill、PRD 模板、日志目录和校验脚本。因此当前使用统一 `init` 更准确。

既有项目与新项目的差异不在安装动作，而在安装后的治理节奏：既有项目会通过生成的 Agent/Skill 在后续任务中逐步回填现有事实。

### 为什么脚本不直接调用大模型分析项目？

这是有意设计。Bootstrap 保持离线、确定、可审计，不要求 API Key、模型选择或外部网络，也不在安装阶段猜测业务事实。语义理解交给后续 AI Agent 和开发者确认，避免把未经验证的内容写进 PRD。

### 既有项目接入后，PRD 什么时候变完整？

不会在安装瞬间完整。它会在后续任务中逐步完整：当某次需求涉及某个页面、接口、模块或数据结构时，AI 会先检查相关 PRD 是否足够描述当前真实行为；如果不足，就先补齐相关范围的 Baseline PRD，再继续开发。

### 用户是否还需要学习一套复杂流程？

不需要每次手动执行复杂流程。用户主要需要做到两点：先运行初始化命令；后续让 AI 从项目入口文件进入。具体的读 PRD、查代码、补文档、写日志由生成的 `prd-keeper` 规则约束。

### 如果 AI 工具不读取项目入口文件怎么办？

需要显式提醒它：`从 AGENTS.md 进入，按 prd-keeper 流程开发。` 这不是业务需求的一部分，而是让 AI 加载项目本地治理规则的入口提示。

---

## 与成熟工程治理实践的关系

PRD Keeper Bootstrap 不是某个单一标准的直接实现，而是面向 AI 辅助软件开发场景，将多种成熟工程治理思想组合成一套轻量、项目内可落地的工作模式。

| 成熟实践 | 在 PRD Keeper 中的体现 |
| --- | --- |
| SDLC Governance | 以软件生命周期视角治理需求、开发、验证和维护 |
| Requirements Traceability | 建立需求、模块、代码变更和日志之间的追溯关系 |
| Docs-as-Code | 将 PRD、架构说明、模块说明和日志纳入版本控制 |
| ADR 思想 | 对重要设计背景、决策和影响进行记录 |
| Quality Gate | 通过校验脚本检查治理结构和必要记录 |
| Policy-as-Code | 将 AI 开发规则写入项目本地 Skill 和入口文件 |
| AI Governance | 对 AI Agent 的行为边界、输入依据和输出责任进行约束 |

可以把它理解为一种：

> **轻量级、项目内、面向 Agent 的 AI-SDLC 治理模式。**

---

## Roadmap

计划中的能力包括：

- `--dry-run`：预览初始化内容，不实际写入文件
- `scan`：静态扫描目标项目，生成项目清单、技术栈线索和 Baseline PRD 回填清单
- `upgrade`：升级已有 PRD Keeper Workspace 的治理模板，尽量避免覆盖本地定制
- `prd-keeper.config.yaml`：支持配置化初始化
- 技术栈模板：例如 Go + Vue、Node + React、Python + FastAPI
- GitHub Actions：在 CI 中校验 PRD Keeper 结构和日志规则
- PRD 日志索引：自动生成变更日志索引
- 全局 Skill 安装模式：将 Bootstrap 能力沉淀为可复用 Agent Skill
- 团队规则扩展：支持组织级治理规范叠加到项目本地规则

后续如果 `scan` 能力与初始化能力形成明显差异，可以再进一步演进为更完整的既有项目接入流程。但当前版本保持统一 `init` 更准确，也更容易理解。

---

## Slogan

```text
Bootstrap auditable PRD-first AI-assisted software development.
```

中文：

```text
一键初始化 PRD-first 可审计 AI 辅助研发闭环。
```

---

## License

建议使用 MIT License，方便个人和团队自由使用、修改和扩展。
