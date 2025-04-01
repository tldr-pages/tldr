# gio trash

> 将文件移动到回收站。
> 由 GNOME 用于处理回收站。
> 更多信息：<https://manned.org/gio.1>.

- 将特定文件移动到回收站：

`gio trash {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 列出回收站中的项目：

`gio trash --list`

- 使用项目 ID 从回收站中恢复特定项目：

`gio trash trash://{{id}}`