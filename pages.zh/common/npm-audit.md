# npm 审计

> 扫描项目依赖中的已知漏洞。
> 报告漏洞并建议修复方案。
> 更多信息：<https://docs.npmjs.com/cli/npm-audit>。

- 扫描项目的依赖以查找已知漏洞：

`npm audit`

- 自动修复项目依赖中的漏洞：

`npm audit fix`

- 强制自动修复有漏洞的依赖：

`npm audit fix {{-f|--force}}`

- 更新锁文件而不修改 `node_modules` 目录：

`npm audit fix --package-lock-only`

- 执行干运行。模拟修复过程而不进行任何更改：

`npm audit fix --dry-run`

- 以 JSON 格式输出审计结果：

`npm audit --json`

- 配置审计仅在高于指定严重性级别的漏洞时失败：

`npm audit --audit-level={{info|low|moderate|high|critical}}`