# aws amplify

> 用于构建安全、可扩展的移动和网页应用程序的开发平台。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html>。

- 创建一个新的 Amplify 应用：

`aws amplify create-app --name {{app_name}} --description {{description}} --repository {{repo_url}} --platform {{platform}} --environment-variables {{env_vars}} --tags {{tags}}`

- 删除一个现有的 Amplify 应用：

`aws amplify delete-app --app-id {{app_id}}`

- 获取特定 Amplify 应用的详细信息：

`aws amplify get-app --app-id {{app_id}}`

- 列出所有 Amplify 应用：

`aws amplify list-apps`

- 更新 Amplify 应用的设置：

`aws amplify update-app --app-id {{app_id}} --name {{new_name}} --description {{new_description}} --repository {{new_repo_url}} --environment-variables {{new_env_vars}} --tags {{new_tags}}`

- 向 Amplify 应用添加一个新的后端环境：

`aws amplify create-backend-environment --app-id {{app_id}} --environment-name {{env_name}} --deployment-artifacts {{artifacts}}`

- 从 Amplify 应用中移除一个后端环境：

`aws amplify delete-backend-environment --app-id {{app_id}} --environment-name {{env_name}}`

- 列出 Amplify 应用中的所有后端环境：

`aws amplify list-backend-environments --app-id {{app_id}}`