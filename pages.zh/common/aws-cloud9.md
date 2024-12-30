# aws cloud9

> 管理 Cloud9 - 一系列在云中编写、构建、运行、测试、调试和发布软件的工具。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/index.html>。

- 列出所有 Cloud9 开发环境标识符：

`aws cloud9 list-environments`

- 创建一个 Cloud9 开发环境：

`aws cloud9 create-environment-ec2 --name {{name}} --instance-type {{instance_type}}`

- 显示 Cloud9 开发环境的信息：

`aws cloud9 describe-environments --environment-ids {{environment_ids}}`

- 向 Cloud9 开发环境添加环境成员：

`aws cloud9 create-environment-membership --environment-id {{environment_id}} --user-arn {{user_arn}} --permissions {{permissions}}`

- 显示 Cloud9 开发环境的状态信息：

`aws cloud9 describe-environment-status --environment-id {{environment_id}}`

- 删除一个 Cloud9 环境：

`aws cloud9 delete-environment --environment-id {{environment_id}}`

- 从开发环境中删除一个环境成员：

`aws cloud9 delete-environment-membership --environment-id {{environment_id}} --user-arn {{user_arn}}`