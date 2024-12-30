# pnpm 审计

> 扫描项目依赖。
> 检查已安装包的已知安全问题。
> 更多信息：<https://pnpm.io/cli/audit>。

- 识别项目中的漏洞：

`pnpm audit`

- 自动修复漏洞：

`pnpm audit fix`

- 生成 JSON 格式的安全报告：

`pnpm audit --json > {{path/to/audit-report.json}}`

- 仅审计 [D]ev 依赖：

`pnpm audit --dev`

- 仅审计 [P]roduction 依赖：

`pnpm audit --prod`

- 从审计中排除可选依赖：

`pnpm audit --no-optional`

- 在审计过程中忽略注册表错误：

`pnpm audit --ignore-registry-errors`

- 按严重性过滤建议（低、中、高、严重）：

`pnpm audit --audit-level {{severity}}`