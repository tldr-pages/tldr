# cf

> 管理 Cloud Foundry 上的应用和服务。
> 更多信息：<https://docs.cloudfoundry.org>.

- 登录 Cloud Foundry API：

`cf login -a {{api_url}}`

- 使用默认设置推送应用：

`cf push {{app_name}}`

- 查看您的组织可访问的服务：

`cf marketplace`

- 创建服务实例：

`cf create-service {{service}} {{plan}} {{service_name}}`

- 将应用连接到服务：

`cf bind-service {{app_name}} {{service_name}}`

- 运行应用中包含的脚本，但独立运行：

`cf run-task {{app_name}} "{{script_command}}" --name {{task_name}}`

- 与运行应用的 VM 进行交互式 SSH 会话：

`cf ssh {{app_name}}`

- 查看应用最近的日志转储：

`cf logs {{app_name}} --recent`