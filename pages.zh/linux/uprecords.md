# uprecords

> 显示历史正常运行记录的摘要。
> 更多信息：<https://manned.org/uprecords>。

- 显示前10个历史正常运行记录的摘要：

`uprecords`

- 显示前25个记录：

`uprecords -m {{25}}`

- 显示重启之间的停机时间，而不是内核版本：

`uprecords -d`

- 显示最近的重启：

`uprecords -B`

- 不截断信息：

`uprecords -w`