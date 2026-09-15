# timeshift

> 系统快照还原工具。
> 更多信息：<https://manned.org/timeshift>。

- 查看快照列表：

`sudo timeshift --list`

- 创建新快照（按计划执行）：

`sudo timeshift --check`

- 创建新快照（强制创建）：

`sudo timeshift --create`

- 还原快照（交互式选择要还原的快照）：

`sudo timeshift --restore`

- 还原指定快照：

`sudo timeshift --restore --snapshot '{{快照名称}}'`

- 删除指定快照：

`sudo timeshift --delete --snapshot '{{快照名称}}'`
