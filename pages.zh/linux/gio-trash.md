# gio 垃圾箱

> 将文件移动到垃圾箱。
> 由 GNOME 用于处理垃圾箱。
> 更多信息：<https://manned.org/gio.1>。

- 将特定文件移动到垃圾箱：

`gio trash {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 列出垃圾箱中的项目：

`gio trash --list`

- 使用其 ID 从垃圾箱中恢复特定项目：

`gio trash trash://{{id}}`