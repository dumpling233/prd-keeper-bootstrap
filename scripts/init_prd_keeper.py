#!/usr/bin/env python3
"""Install a project-local PRD Keeper governance loop into any repository."""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates"


TEXT_EXTENSIONS = {
    ".md",
    ".yaml",
    ".yml",
    ".py",
    ".tpl",
}


@dataclass
class InstallResult:
    written: list[Path]
    skipped: list[Path]
    log_file: Path


def git_value(key: str, cwd: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "config", key],
            cwd=cwd,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return ""
    return result.stdout.strip()


def git_writer(cwd: Path) -> str:
    return git_value("user.name", cwd) or git_value("user.email", cwd) or "unknown"


def safe_slug(value: str) -> str:
    safe = re.sub(r'[\\/:*?"<>|\s]+', "-", value.strip())
    safe = safe.strip(".-")
    return safe or "unknown"


def render(text: str, variables: dict[str, str]) -> str:
    for key, value in variables.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def output_path_for(template_file: Path, target: Path) -> Path:
    rel = template_file.relative_to(TEMPLATE_ROOT)
    parts = list(rel.parts)
    filename = parts[-1]
    if filename.endswith(".tpl"):
        filename = filename[:-4]
    parts[-1] = filename
    return target.joinpath(*parts)


def is_text_template(path: Path) -> bool:
    return path.suffix in TEXT_EXTENSIONS or path.name.endswith(".tpl")


def copy_templates(target: Path, variables: dict[str, str], force: bool) -> InstallResult:
    written: list[Path] = []
    skipped: list[Path] = []
    for template_file in sorted(TEMPLATE_ROOT.rglob("*")):
        if template_file.is_dir():
            continue
        destination = output_path_for(template_file, target)
        if destination.exists() and not force:
            skipped.append(destination)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        if is_text_template(template_file):
            content = template_file.read_text(encoding="utf-8")
            destination.write_text(render(content, variables), encoding="utf-8")
        else:
            destination.write_bytes(template_file.read_bytes())
        written.append(destination)

    log_dir = target / "docs" / "prd" / "prd_log"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{variables['DATE_YYYYMMDD']}-{variables['GIT_USER_SLUG']}.md"
    if not log_file.exists() or force:
        log_file.write_text(initial_log(variables), encoding="utf-8")
        written.append(log_file)
    else:
        existing = log_file.read_text(encoding="utf-8").rstrip()
        log_file.write_text(f"{existing}\n\n{initial_log_entry(variables)}", encoding="utf-8")
        written.append(log_file)
    return InstallResult(written=written, skipped=skipped, log_file=log_file)


def initial_log(variables: dict[str, str]) -> str:
    return (
        f"# {variables['DATE_YYYYMMDD']}-{variables['GIT_USER_SLUG']} PRD / 开发变更日志\n\n"
        + initial_log_entry(variables)
    )


def initial_log_entry(variables: dict[str, str]) -> str:
    today = variables["DATE_ISO"]
    writer = variables["GIT_USER"]
    project = variables["PROJECT_NAME"]
    return f"""## {today} - 初始化 PRD-first 可审计 AI 研发闭环

### 编写人
- {writer}

### 请求
- 为 `{project}` 初始化通用 PRD-first 可审计 AI 研发闭环。

### 影响模块
- AI 入口文件。
- 项目内 PRD Keeper Skill。
- 分层 PRD 文档。
- PRD 日志与校验脚本。

### 代码变更
- 新增或更新 `AGENTS.md`、`CODEX.md`、`CLAUDE.md` 薄入口。
- 新增或更新 `.agent/skills/prd-keeper/` 项目内治理 Skill。
- 新增或更新 `docs/prd/` 分层 PRD 模板。

### PRD 更新
- 创建初始 PRD 总入口、产品概览、架构说明、模块索引和 PRD Keeper 模块文档。

### 验证
- 未运行：初始化后请运行 `.agent/skills/prd-keeper/scripts/check_prd_keeper.py`。

### 风险/后续事项
- 模板中的 `待确认` 项需要结合真实代码、配置和用户说明继续填充。
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Install PRD Keeper into a project.")
    parser.add_argument("--target", default=".", help="Target project directory.")
    parser.add_argument("--project-name", help="Project name. Defaults to target folder name.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        raise SystemExit(f"Target does not exist: {target}")
    if not target.is_dir():
        raise SystemExit(f"Target is not a directory: {target}")

    project_name = args.project_name or target.name
    writer = git_writer(target)
    now = datetime.now()
    variables = {
        "PROJECT_NAME": project_name,
        "PROJECT_SLUG": safe_slug(project_name),
        "DATE_YYYYMMDD": now.strftime("%Y%m%d"),
        "DATE_ISO": now.strftime("%Y-%m-%d"),
        "GIT_USER": writer,
        "GIT_USER_SLUG": safe_slug(writer),
    }

    result = copy_templates(target, variables, args.force)
    print(f"Installed PRD Keeper into: {target}")
    print(f"Written files: {len(result.written)}")
    print(f"Skipped existing files: {len(result.skipped)}")
    print(f"Initial log: {result.log_file.relative_to(target)}")
    if result.skipped:
        print("Skipped files:")
        for path in result.skipped:
            print(f"- {path.relative_to(target)}")
    print("Next: fill docs/prd/*.md with project facts, then run the generated check_prd_keeper.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
