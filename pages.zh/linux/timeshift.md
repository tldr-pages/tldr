# timeshift

> 系统还原工具。
> 更多信息：<https://github.com/teejee2008/timeshift>。

- 列出现有快照：

`sudo timeshift --list`

- 创建新快照（如果已安排）：

`sudo timeshift --check`

- 创建新快照（即使未安排）：

`sudo timeshift --create`

- 还原快照（交互式选择要还原的快照）：

`sudo timeshift --restore`

- 还原特定快照：

`sudo timeshift --restore --snapshot '{{snapshot}}'`

- 删除特定快照：

`sudo timeshift --delete --snapshot '{{snapshot}}'`
