# systemd-hwdb

> 硬件数据库管理工具。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-hwdb.html>。

- 更新 `/etc/udev` 中的二进制硬件数据库：

`systemd-hwdb update`

- 查询硬件数据库并打印特定 modalias 的结果：

`systemd-hwdb query {{modalias}}`

- 更新二进制硬件数据库，在任何解析错误时返回非零退出值：

`systemd-hwdb --strict update`

- 更新 `/usr/lib/udev` 中的二进制硬件数据库：

`systemd-hwdb --usr update`

- 在指定根路径中更新二进制硬件数据库：

`systemd-hwdb --root={{path/to/root}} update`