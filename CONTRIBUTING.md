# Contributing / 贡献指南

## SKILL.md 编写规范 / SKILL.md Writing Standards

### ⚠️ 必须中英双语 / Bilingual Required

所有 SKILL.md 的所有内容必须同时包含中文和英文。
All SKILL.md content must include both Chinese and English.

**格式规范 / Format Rules:**

1. **Frontmatter description**：纯中文（ClawHub 卡片展示优先中文）/ Chinese only (ClawHub card displays Chinese first)
   ```yaml
   description: >
     纯中文描述即可。ClawHub 展示时优先取中文。
   ```

2. **标题 / Headings**：中文在前，英文在后，用 `/` 分隔 / Chinese first, English after, separated by `/`
   ```markdown
   ## 标题 / English Title
   ### 子标题 / English Subtitle
   ```

3. **正文内容 / Body content**：中文在先，英文跟在后面 / Chinese first, English follows
   ```markdown
   - 这是中文说明 / This is English description
   - 另一条规则 / Another rule
   ```

4. **检查清单 / Checklist**（每次修改 SKILL.md 后自查 / Self-check after every SKILL.md edit）：
   - [ ] 所有 `##` 和 `###` 标题都有中英双语 / All headings have bilingual text
   - [ ] 所有段落正文都有中英双语 / All body paragraphs have bilingual text
   - [ ] 新增的章节/规则是否补了英文翻译 / New sections have English translations
   - [ ] description 保持纯中文 / description remains Chinese only

### 目录结构 / Directory Structure

```
awesome-skills/
├── <skill-name>/
│   ├── SKILL.md          # 技能定义文件（必须中英双语 / Must be bilingual）
│   └── references/       # 可选：引用文件（模板、代码片段等 / Optional: templates, code snippets, etc.）
├── .github/
│   └── workflows/
│       ├── publish.yml           # 统一发布（所有 skill / Publish all skills）
│       └── publish-<name>.yml    # 单独发布（单个 skill / Publish single skill）
└── CONTRIBUTING.md       # 本文件 / This file
```

### 版本发布 / Version Publishing

- 推送到 `main` 分支（包含 SKILL.md 变更）会自动触发 GitHub Actions 发布到 ClawHub
- Pushing to `main` with SKILL.md changes triggers automatic ClawHub publishing via GitHub Actions
- **推荐单独发布 / Recommended: publish individually**：只推送修改了 SKILL.md 的 skill 子目录的 workflow
- 版本号 / Version: `0.1.<run_number>`（run_number 递增，保证唯一 / run_number increments, guaranteed unique）
- 手动发版 / Manual release：打 tag `v0.2.0` 后推送 / Push a tag like `v0.2.0`
- ClawHub 页面 / ClawHub page：https://clawhub.ai/z-zihan/<slug>
