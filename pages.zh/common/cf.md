# cf

> 管理 Cloud Foundry 上的应用和服务。
> 更多信息：<https://docs.cloudfoundry.org>。

- 登录到 Cloud Foundry API：

`cf login -a {{api_url}}`

- 使用默认设置推送一个应用：

`cf push {{app_name}}`

- 查看您组织可用的服务：

`cf marketplace`

- 创建一个服务实例：

`cf create-service {{service}} {{plan}} {{service_name}}`

- 将应用连接到服务：

`cf bind-service {{app_name}} {{service_name}}`

- 运行包含在应用中的脚本，但独立运行：

`cf run-task {{app_name}} "{{script_command}}" --name {{task_name}}`

- 与托管应用的虚拟机启动交互式 SSH 会话：

`cf ssh {{app_name}}`

- 查看最近应用日志的转储：

`cf logs {{app_name}} --recent`