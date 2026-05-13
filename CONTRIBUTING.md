# Contributing / 贡献指南

## SKILL.md 编写规范 / SKILL.md Writing Standards

### ⚠️ 必须中英双语 / Bilingual Required

所有 SKILL.md 的所有内容必须同时包含中文和英文。

**格式规范 / Format Rules:**

1. **Frontmatter description**：纯中文（ClawHub 卡片展示优先中文）
   ```yaml
   description: >
     这是中文描述。This is English description is NOT needed here.
     description is Chinese only.
   ```

2. **标题 / Headings**：中文在前，英文在后，用 `/` 分隔
   ```markdown
   ## 标题 / English Title
   ### 子标题 / English Subtitle
   ```

3. **正文内容 / Body content**：中文在先，英文跟在后面
   ```markdown
   - 这是中文说明 / This is English description
   - 另一条规则 / Another rule
   ```

4. **检查清单 / Checklist**（每次修改 SKILL.md 后自查）：
   - [ ] 所有 `##` 和 `###` 标题都有中英双语
   - [ ] 所有段落正文都有中英双语
   - [ ] 新增的章节/规则是否补了英文翻译
   - [ ] description 保持纯中文

### 目录结构 / Directory Structure

```
awesome-skills/
├── <skill-name>/
│   ├── SKILL.md          # 技能定义文件（必须中英双语）
│   └── references/       # 可选：引用文件（模板、代码片段等）
├── .github/
│   └── workflows/
│       └── publish.yml   # ClawHub 自动发布
└── CONTRIBUTING.md       # 本文件
```

### 版本发布 / Version Publishing

- 推送到 `main` 分支（包含 SKILL.md 变更）会自动触发 GitHub Actions 发布到 ClawHub
- 版本号：`0.1.<run_number>`（run_number 递增，保证唯一）
- 手动发版：打 tag `v0.2.0` 后推送，使用 tag 版本号
- ClawHub 页面：https://clawhub.ai/z-zihan/<slug>
