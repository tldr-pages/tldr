# pnpm audit

> 扫描项目依赖。
> 检查已安装的包中是否有已知的安全问题。
> 更多信息：<https://pnpm.io/cli/audit>。

- 识别项目中的漏洞：

`pnpm audit`

- 自动修复漏洞：

`pnpm audit fix`

- 生成 JSON 格式的安全报告：

`pnpm audit --json > {{path/to/audit-report.json}}`

- 仅审计开发依赖：

`pnpm audit {{[-D|--dev]}}`

- 仅审计生产依赖：

`pnpm audit {{[-P|--prod]}}`

- 从审计中排除可选依赖：

`pnpm audit --no-optional`

- 在审计过程中忽略注册表错误：

`pnpm audit --ignore-registry-errors`

- 按严重性（低、中、高、严重）过滤安全建议：

`pnpm audit --audit-level {{severity}}`
