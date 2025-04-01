# aws amplify

> 用于构建安全、可扩展的移动和网络应用程序的开发平台。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html>.

- 创建一个新的 Amplify 应用程序：

`aws amplify create-app --name {{app_name}} --description {{description}} --repository {{repo_url}} --platform {{platform}} --environment-variables {{env_vars}} --tags {{tags}}`

- 删除现有的 Amplify 应用程序：

`aws amplify delete-app --app-id {{app_id}}`

- 获取特定 Amplify 应用程序的详细信息：

`aws amplify get-app --app-id {{app_id}}`

- 列出所有 Amplify 应用程序：

`aws amplify list-apps`

- 更新 Amplify 应用程序的设置：

`aws amplify update-app --app-id {{app_id}} --name {{new_name}} --description {{new_description}} --repository {{new_repo_url}} --environment-variables {{new_env_vars}} --tags {{new_tags}}`

- 为 Amplify 应用程序添加一个新的后端环境：

`aws amplify create-backend-environment --app-id {{app_id}} --environment-name {{env_name}} --deployment-artifacts {{artifacts}}`

- 从 Amplify 应用程序中删除一个后端环境：

`aws amplify delete-backend-environment --app-id {{app_id}} --environment-name {{env_name}}`

- 列出 Amplify 应用程序中的所有后端环境：

`aws amplify list-backend-environments --app-id {{app_id}}`
