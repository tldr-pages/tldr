# serverless

> 用于在 AWS、Google Cloud、Azure 和 IBM OpenWhisk 上部署和操作无服务器架构的工具包。
> 命令可以使用 `serverless` 命令或其别名 `sls` 运行。
> 更多信息：<https://serverless.com/>。

- 创建无服务器项目：

`serverless create`

- 从模板创建无服务器项目：

`serverless create --template {{template_name}}`

- 部署到云提供商：

`serverless deploy`

- 显示无服务器项目的信息：

`serverless info`

- 调用已部署的函数：

`serverless invoke -f {{function_name}}`

- 跟踪项目的日志：

`serverless logs -t`