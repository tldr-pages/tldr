# aws amplify

> 用于构建安全、可扩展的移动和 Web 应用程序的开发平台。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/amplify/>.

- 创建一个新的 Amplify 应用：

`aws amplify create-app --name {{应用名称}} --description {{描述}} --repository {{仓库 URL}} --platform {{平台}} --environment-variables {{环境变量}} --tags {{标签}}`

- 删除一个现有的 Amplify 应用：

`aws amplify delete-app --app-id {{应用 ID}}`

- 获取指定 Amplify 应用的详细信息：

`aws amplify get-app --app-id {{应用 ID}}`

- 列出所有 Amplify 应用：

`aws amplify list-apps`

- 更新 Amplify 应用的设置：

`aws amplify update-app --app-id {{应用 ID}} --name {{新名称}} --description {{新描述}} --repository {{新仓库 URL}} --environment-variables {{新环境变量}} --tags {{新标签}}`

- 为 Amplify 应用添加一个新的后端环境：

`aws amplify create-backend-environment --app-id {{应用 ID}} --environment-name {{环境名称}} --deployment-artifacts {{部署构件}}`

- 从 Amplify 应用中移除一个后端环境：

`aws amplify delete-backend-environment --app-id {{应用 ID}} --environment-name {{环境名称}}`

- 列出 Amplify 应用中的所有后端环境：

`aws amplify list-backend-environments --app-id {{应用 ID}}`
