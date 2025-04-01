# npm audit

> 扫描项目依赖项中的已知漏洞。
> 报告漏洞并建议修复方法。
> 更多信息：<https://docs.npmjs.com/cli/npm-audit>.

- 扫描项目依赖项中的已知漏洞：

`npm audit`

- 自动修复项目依赖项中的漏洞：

`npm audit fix`

- 强制自动修复有漏洞的依赖项：

`npm audit fix {{[-f|--force]}}`

- 更新锁定文件而不修改 `node_modules` 目录：

`npm audit fix --package-lock-only`

- 执行模拟修复过程，不进行任何实际更改：

`npm audit fix --dry-run`

- 以 JSON 格式输出审计结果：

`npm audit --json`

- 配置审计，仅在漏洞严重性超过指定级别时失败：

`npm audit --audit-level={{info|low|moderate|high|critical}}`
