# aws 历史记录

> 打印 AWS CLI 命令的命令行历史记录（必须启用 AWS CLI 命令的历史记录）。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/history/>。

- 列出带有命令 ID 的命令历史：

`aws history list`

- 显示与特定命令相关的事件，给定命令 ID：

`aws history show {{command_id}}`