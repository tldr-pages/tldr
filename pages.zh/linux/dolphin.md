# dolphin

> KDE 的文件管理器，用于管理和浏览文件及目录。
> 相关命令：`nautilus`, `caja`, `thunar`, `ranger`。
> 更多信息：<https://apps.kde.org/dolphin/>。

- 启动文件管理器：

`dolphin`

- 打开特定的目录：

`dolphin {{path/to/directory1 path/to/directory2 ...}}`

- 打开文件管理器并选择特定的文件或目录：

`dolphin --select {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 打开新窗口：

`dolphin --new-window`

- 在分割视图中打开特定的目录：

`dolphin --split {{path/to/directory1}} {{path/to/directory2}}`

- 启动守护进程（仅在需要使用 D-Bus 接口时使用）：

`dolphin --daemon`

- 显示帮助信息：

`dolphin --help`