# func

> Azure Functions Core Tools：本地开发和测试 Azure Functions。
> 本地函数可以连接到实时 Azure 服务，并可以将函数应用部署到 Azure 订阅。
> 更多信息：<https://learn.microsoft.com/azure/azure-functions/functions-run-local>。

- 创建一个新的函数项目：

`func init {{project}}`

- 创建一个新的函数：

`func new`

- 本地运行函数：

`func start`

- 将代码发布到 Azure 中的函数应用：

`func azure functionapp publish {{function}}`

- 从现有的函数应用下载所有设置：

`func azure functionapp fetch-app-settings {{function}}`

- 获取特定存储帐户的连接字符串：

`func azure storage fetch-connection-string {{storage_account}}`