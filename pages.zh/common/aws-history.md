# aws history

> 打印 AWS CLI 命令的历史记录（必须启用 AWS CLI 命令的历史记录）。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/history/>.

- 列出带有命令 ID 的命令历史记录：

`aws history list`

- 显示与给定命令 ID 相关的事件：

`aws history show {{command_id}}`