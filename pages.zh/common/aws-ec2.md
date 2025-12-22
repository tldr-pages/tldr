# aws ec2

> 管理 AWS EC2 实例和卷。
> AWS EC2 在 AWS 云中提供安全且可伸缩的计算容量，用于更快速地开发和部署应用程序。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/ec2/>.

- 显示特定实例的信息：

`aws ec2 describe-instances --instance-ids {{实例 ID}}`

- 显示所有实例的信息：

`aws ec2 describe-instances`

- 显示所有 EC2 卷的信息：

`aws ec2 describe-volumes`

- 删除一个 EC2 卷：

`aws ec2 delete-volume --volume-id {{卷 ID}}`

- 从一个 EC2 卷创建快照：

`aws ec2 create-snapshot --volume-id {{卷 ID}}`

- 列出可用的 AMI（Amazon 机器映像）：

`aws ec2 describe-images`

- 显示所有可用的 EC2 命令列表：

`aws ec2 help`

- 显示特定 EC2 子命令的帮助信息：

`aws ec2 {{子命令}} help`
