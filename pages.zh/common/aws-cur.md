# aws cur

> 创建、查询和删除 AWS 使用报告定义。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>。

- 从 JSON 文件创建 AWS 成本和使用报告定义：

`aws cur put-report-definition --report-definition file://{{path/to/report_definition.json}}`

- 列出登录账户定义的使用报告定义：

`aws cur describe-report-definitions`

- 删除使用报告定义：

`aws cur --region {{aws_region}} delete-report-definition --report-name {{report}}`
