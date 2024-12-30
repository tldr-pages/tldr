# sam

> AWS无服务器应用程序模型（SAM）CLI。
> 更多信息：<https://github.com/awslabs/aws-sam-cli>。

- 初始化一个无服务器应用程序：

`sam init`

- 使用特定运行时初始化无服务器应用程序：

`sam init --runtime {{python3.7}}`

- 打包SAM应用程序：

`sam package`

- 构建您的Lambda函数代码：

`sam build`

- 在本地运行您的无服务器应用程序：

`sam local start-api`

- 部署AWS SAM应用程序：

`sam deploy`