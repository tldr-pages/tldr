# aws cloud9

> 管理 Cloud9 —— 一组用于在云中编写代码、构建、运行、测试、调试和发布软件的工具。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/cloud9/>.

- 列出所有 Cloud9 开发环境标识符：

`aws cloud9 list-environments`

- 创建一个 Cloud9 开发环境：

`aws cloud9 create-environment-ec2 --name {{名称}} --instance-type {{实例类型}}`

- 显示 Cloud9 开发环境的信息：

`aws cloud9 describe-environments --environment-ids {{环境 ID 列表}}`

- 向 Cloud9 开发环境添加一个环境成员：

`aws cloud9 create-environment-membership --environment-id {{环境 ID}} --user-arn {{用户 ARN}} --permissions {{权限}}`

- 显示 Cloud9 开发环境的状态信息：

`aws cloud9 describe-environment-status --environment-id {{环境 ID}}`

- 删除一个 Cloud9 环境：

`aws cloud9 delete-environment --environment-id {{环境 ID}}`

- 从开发环境中删除一个环境成员：

`aws cloud9 delete-environment-membership --environment-id {{环境 ID}} --user-arn {{用户 ARN}}`
