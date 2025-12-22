# aws lambda

> 使用 AWS Lambda，这是一个无需预置或管理服务器即可运行代码的计算服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- 运行一个函数：

`aws lambda invoke --function-name {{名称}} {{路径/到/response.json}}`

- 使用 JSON 格式的输入负载运行一个函数：

`aws lambda invoke --function-name {{名称}} --payload {{json}} {{路径/到/response.json}}`

- 列出函数：

`aws lambda list-functions`

- 显示函数的配置：

`aws lambda get-function-configuration --function-name {{名称}}`

- 列出函数别名：

`aws lambda list-aliases --function-name {{名称}}`

- 显示函数的预留并发配置：

`aws lambda get-function-concurrency --function-name {{名称}}`

- 列出哪些 AWS 服务可以调用该函数：

`aws lambda get-policy --function-name {{名称}}`
