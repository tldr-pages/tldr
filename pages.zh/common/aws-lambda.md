# AWS Lambda

> 使用 AWS Lambda，这是一项计算服务，可以在不配置或管理服务器的情况下运行代码。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- 运行一个函数：

`aws lambda invoke --function-name {{name}} {{path/to/response.json}}`

- 以 JSON 格式的输入负载运行一个函数：

`aws lambda invoke --function-name {{name}} --payload {{json}} {{path/to/response.json}}`

- 列出函数：

`aws lambda list-functions`

- 显示函数的配置：

`aws lambda get-function-configuration --function-name {{name}}`

- 列出函数别名：

`aws lambda list-aliases --function-name {{name}}`

- 显示函数的保留并发配置：

`aws lambda get-function-concurrency --function-name {{name}}`

- 列出哪些 AWS 服务可以调用该函数：

`aws lambda get-policy --function-name {{name}}`