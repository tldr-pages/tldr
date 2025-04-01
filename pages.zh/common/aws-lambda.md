# aws lambda

> 使用 AWS Lambda，一种无需配置或管理服务器即可运行代码的计算服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- 运行一个函数：

`aws lambda invoke --function-name {{name}} {{path/to/response.json}}`

- 使用 JSON 格式的输入负载运行一个函数：

`aws lambda invoke --function-name {{name}} --payload {{json}} {{path/to/response.json}}`

- 列出所有函数：

`aws lambda list-functions`

- 显示函数的配置信息：

`aws lambda get-function-configuration --function-name {{name}}`

- 列出函数的别名：

`aws lambda list-aliases --function-name {{name}}`

- 显示函数的预留并发配置：

`aws lambda get-function-concurrency --function-name {{name}}`

- 列出可以调用该函数的 AWS 服务：

`aws lambda get-policy --function-name {{name}}`