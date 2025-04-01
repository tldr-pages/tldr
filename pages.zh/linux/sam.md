# sam

> AWS Serverless Application Model (SAM) 命令行工具。
> 更多信息：<https://github.com/awslabs/aws-sam-cli>。

- 初始化一个无服务器应用：

`sam init`

- 使用特定运行时初始化一个无服务器应用：

`sam init --runtime {{python3.7}}`

- 打包 SAM 应用：

`sam package`

- 构建 Lambda 函数代码：

`sam build`

- 本地运行无服务器应用：

`sam local start-api`

- 部署 AWS SAM 应用：

`sam deploy`