# 🧰 OpenClaw Team Skills

团队共享的 OpenClaw AI Agent 技能库。一个 skill 就是一份 `SKILL.md`，安装后 Agent 会自动按需加载。

## 快速开始

```bash
git clone <repo-url>
cd skills
bash install.sh    # 软链接所有 skill 到 ~/.openclaw-autoclaw/skills/
```

更新也一样：`git pull && bash install.sh`。

---

## Skill 一览

### 🤖 code-review — 代码审查

资深代码审查专家。从正确性、回归风险、兼容性、稳定性、性能、安全性、上下游影响等多维度审查代码变更。输出结构化、可用于合入决策的审查结论。

```
触发："review 这段代码" / "审查这个文件" / 贴 diff
```

### 🏗️ fe-cli — 前端项目脚手架

一键创建规范化前端项目，自动生成标准目录结构、共享代码层（请求封装 / 样式 / 工具函数 / 环境配置 / AI 可读文档）、Vite + TypeScript 配置。

| 子 Skill | 类型 | 触发关键词 |
|---|---|---|
| `fe-cli-web` | Web SPA | 官网、网页、SPA |
| `fe-cli-admin` | 后台管理 | 后台、管理、Admin、Dashboard |
| `fe-cli-h5` | 移动端 H5 | 移动、H5、手机、微信 H5 |
| `fe-cli-electron` | 桌面应用 | 桌面、Electron、客户端 |
| `fe-cli-ssr` | 服务端渲染 | SSR、Next.js、Nuxt、SEO |
| `fe-cli-miniapp` | 小程序 | 小程序、微信小程序、MiniApp |

**使用：**

```
"创建一个 React + Ant Design 后台项目，叫 order-admin"
"新建一个移动端 H5 项目"
"初始化 Electron 桌面应用"
```

**技术栈规范：**

| 约束 | 值 |
|---|---|
| 包管理器 | pnpm |
| CSS 预处理器 | Sass (SCSS) |
| 网络库 | native fetch（不用 axios） |
| 路径别名 | `@/` → `src/` |
| Node 版本 | 18+ |
| 响应式断点 | 768px / 1024px |

---

## 目录结构

```
skills/
├── README.md
├── install.sh              # 一键安装脚本
├── code-review/
│   └── SKILL.md            # 代码审查
└── fe-cli/
    ├── SKILL.md            # 主控：类型识别 + 共享层生成
    ├── references/         # 共享模板（按需读取，不触发安装）
    │   ├── shared-base.md
    │   ├── shared-config.md
    │   └── ai-project-md.md
    ├── web/SKILL.md
    ├── admin/SKILL.md
    ├── h5/SKILL.md
    ├── electron/SKILL.md
    ├── ssr/SKILL.md
    └── miniapp/SKILL.md
```

> `references/` 下的 `.md` 不会被 `install.sh` 发现（没有名为 `SKILL.md`），不会产生多余链接。

---

## 贡献新 Skill

1. 在仓库根目录创建文件夹 + `SKILL.md`：

```
my-skill/
└── SKILL.md
```

2. **SKILL.md 必须包含 YAML frontmatter**：

```yaml
---
name: my-skill
description: >
  一句话描述。支持多关键词触发。
  例如：Use when user asks for X, mentions Y, or wants to Z.
---
```

3. 提交 push。团队成员 `git pull && bash install.sh` 即可获取。

---

## 设计原则

- **按需加载**：Skill 内容只在触发时读入，不占用日常上下文
- **独立触发**：即使嵌套在子目录下，`install.sh` 也会为每个 `SKILL.md` 创建独立顶层链接
- **模板分离**：共享代码模板放在 `references/`，不影响 skill 发现
- **不重复造轮子**：优先复用 OpenClaw 已有能力，skill 只补充领域知识
