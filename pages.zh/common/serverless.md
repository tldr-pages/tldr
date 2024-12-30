# 无服务器

> 用于在 AWS、谷歌云、Azure 和 IBM OpenWhisk 上部署和操作无服务器架构的工具包。
> 可以使用 `serverless` 命令或其别名 `sls` 来运行命令。
> 更多信息：<https://serverless.com/>.

- 创建一个无服务器项目：

`serverless create`

- 从模板创建一个无服务器项目：

`serverless create --template {{template_name}}`

- 部署到云服务提供商：

`serverless deploy`

- 显示有关无服务器项目的信息：

`serverless info`

- 调用已部署的函数：

`serverless invoke -f {{function_name}}`

- 跟踪项目的日志：

`serverless logs -t`