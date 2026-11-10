# ant-design

9 skills sparse-checked-out from <https://github.com/ant-design/ant-design> (MIT) — the
full repo is ~280MB of component source/tests/docs; only its `.agents/skills/` and
`public/.well-known/agent-skills/` were pulled (`.claude/skills` and `.cursor/skills` are
symlinks to `.agents/skills`, so nothing was duplicated).

## `usage-skills/` (3) — for building with Ant Design

- **antd-component-lookup** — Look up Ant Design React component documentation, props, and usage examples.
- **antd-migration** — Migrate between Ant Design major versions (v4 → v5, breaking API changes).
- **antd-theme-customization** — Customize theme via Design Tokens and `ConfigProvider` (colors, spacing, visual style).

## `maintainer-skills/` (6) — for maintaining the ant-design repo itself

Narrow, repo-specific — only useful if actually contributing to ant-design/ant-design.
Mostly Chinese-language:

- **changelog-collect** — 收集两个版本之间的 PR 信息，整理 changelog 草稿。
- **antd-commit-msg** — Generate a one-line commit message matching the repo's style from staged changes.
- **antd-create-pr** — Create PRs using the repo's official PR templates.
- **antd-issue-reply** — Reply to GitHub issues per Ant Design's maintainer guidelines (bug vs. feature classification, labels, tone).
- **antd-test-review** — 审查测试用例是否值得保留（重复/锁定实现细节/证明力不足）。
- **antd-version-release** — 版本发布工作流（release PR、版本号、npm publish 校验）。
