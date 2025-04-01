# aws ec2

> 管理 AWS EC2 实例和卷。
> AWS EC2 在 AWS 云中提供安全且可扩展的计算能力，用于加快应用程序的开发和部署。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>。

- 显示特定实例的信息：

`aws ec2 describe-instances --instance-ids {{instance_id}}`

- 显示所有实例的信息：

`aws ec2 describe-instances`

- 显示所有 EC2 卷的信息：

`aws ec2 describe-volumes`

- 删除 EC2 卷：

`aws ec2 delete-volume --volume-id {{volume_id}}`

- 从 EC2 卷创建快照：

`aws ec2 create-snapshot --volume-id {{volume_id}}`

- 列出可用的 AMI（Amazon 机器镜像）：

`aws ec2 describe-images`

- 显示所有可用的 EC2 命令列表：

`aws ec2 help`

- 显示特定 EC2 子命令的帮助信息：

`aws ec2 {{subcommand}} help`
