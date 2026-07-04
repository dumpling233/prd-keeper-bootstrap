#!/usr/bin/env node

import { spawnSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const initScript = path.join(root, "scripts", "init_prd_keeper.py");
const packageJson = path.join(root, "package.json");

const rawArgs = process.argv.slice(2);

function printHelp() {
  console.log(`PRD Keeper Bootstrap

Usage:
  prd-keeper init --target <target-project> --project-name <project-name> [--force]
  prd-keeper --help
  prd-keeper --version

Examples:
  prd-keeper init --target . --project-name my-project
  prd-keeper init --target D:\\work\\your-project --project-name your-project
  npx prd-keeper-bootstrap init --target . --project-name my-project

Requirements:
  Node.js >= 18
  Python >= 3.9
`);
}

function readVersion() {
  try {
    return JSON.parse(readFileSync(packageJson, "utf8")).version ?? "unknown";
  } catch {
    return "unknown";
  }
}

function normalizeArgs(args) {
  if (args.length === 0 || args[0] === "--help" || args[0] === "-h" || args[0] === "help") {
    return { command: "help", args: [] };
  }
  if (args[0] === "--version" || args[0] === "-v") {
    return { command: "version", args: [] };
  }
  if (args[0] === "init") {
    return { command: "init", args: args.slice(1) };
  }
  if (args[0].startsWith("-")) {
    return { command: "init", args };
  }
  return { command: args[0], args: args.slice(1) };
}

function parsePythonVersion(output) {
  const match = /Python\s+(\d+)\.(\d+)(?:\.(\d+))?/.exec(output);
  if (!match) {
    return null;
  }
  return {
    major: Number(match[1]),
    minor: Number(match[2]),
    patch: Number(match[3] ?? "0"),
  };
}

function isSupportedPython(version) {
  return version.major > 3 || (version.major === 3 && version.minor >= 9);
}

function pythonCandidates() {
  const candidates = [];
  if (process.env.PRD_KEEPER_PYTHON) {
    candidates.push({
      command: process.env.PRD_KEEPER_PYTHON,
      prefix: [],
      label: "PRD_KEEPER_PYTHON",
    });
  }
  if (process.platform === "win32") {
    candidates.push(
      { command: "py", prefix: ["-3"], label: "py -3" },
      { command: "python", prefix: [], label: "python" },
      { command: "python3", prefix: [], label: "python3" },
    );
  } else {
    candidates.push(
      { command: "python3", prefix: [], label: "python3" },
      { command: "python", prefix: [], label: "python" },
    );
  }
  return candidates;
}

function findPython() {
  const failures = [];
  for (const candidate of pythonCandidates()) {
    const result = spawnSync(candidate.command, [...candidate.prefix, "--version"], {
      encoding: "utf8",
      windowsHide: true,
    });
    if (result.error || result.status !== 0) {
      failures.push(`${candidate.label}: unavailable`);
      continue;
    }
    const versionText = `${result.stdout ?? ""}${result.stderr ?? ""}`.trim();
    const version = parsePythonVersion(versionText);
    if (!version) {
      failures.push(`${candidate.label}: cannot parse version (${versionText || "empty output"})`);
      continue;
    }
    if (!isSupportedPython(version)) {
      failures.push(`${candidate.label}: ${versionText} < 3.9`);
      continue;
    }
    return candidate;
  }
  const message = [
    "未找到可用的 Python >= 3.9。",
    "请安装 Python >= 3.9，或设置 PRD_KEEPER_PYTHON 指向可执行的 Python。",
    "",
    "尝试结果：",
    ...failures.map((item) => `- ${item}`),
  ].join("\n");
  throw new Error(message);
}

function runInit(args) {
  if (!existsSync(initScript)) {
    throw new Error(`找不到初始化脚本：${initScript}`);
  }
  const python = findPython();
  const result = spawnSync(python.command, [...python.prefix, initScript, ...args], {
    stdio: "inherit",
    windowsHide: false,
  });
  if (result.error) {
    throw result.error;
  }
  if (result.signal) {
    process.kill(process.pid, result.signal);
    return;
  }
  process.exit(result.status ?? 1);
}

try {
  const parsed = normalizeArgs(rawArgs);
  if (parsed.command === "help") {
    printHelp();
    process.exit(0);
  }
  if (parsed.command === "version") {
    console.log(readVersion());
    process.exit(0);
  }
  if (parsed.command !== "init") {
    console.error(`未知命令：${parsed.command}`);
    console.error("运行 `prd-keeper --help` 查看用法。");
    process.exit(1);
  }
  runInit(parsed.args);
} catch (error) {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
}
