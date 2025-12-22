> 创建、查询和删除 AWS 使用情况报告定义。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/cur/>.

- 从一个 JSON 文件创建 AWS 成本和使用情况报告定义：

`aws cur put-report-definition --report-definition file://{{路径/到/report_definition.json}}`

- 列出当前登录账户中定义的使用情况报告定义：

`aws cur describe-report-definitions`

- 删除一个使用情况报告定义：

`aws cur --region {{AWS 区域}} delete-report-definition --report-name {{报告}}`
