# composer audit

> 分析 PHP 项目的依赖关系，以检测已知的安全漏洞并列出受影响的软件包。
> 查看更多：`composer`。
> 更多信息：<https://getcomposer.org/doc/03-cli.md#audit>。

- 检查当前项目中的安全漏洞：

`composer audit`

- 在审核时忽略开发依赖：

`composer audit --no-dev`

- 按输出格式筛选漏洞：

`composer audit --format {{table|plain|json|summary}}`

- 将审核结果以 JSON 格式输出到文件：

`composer audit --format json > audit_report.json`

- 验证项目中特定软件包是否受安全问题影响：

`composer audit {{vendor}}/{{package}}`