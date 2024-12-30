# 海豚

> KDE 的文件管理器，用于管理文件和目录。
> 另见：`nautilus`，`caja`，`thunar`，`ranger`。
> 更多信息：<https://apps.kde.org/dolphin/>。

- 启动文件管理器：

`dolphin`

- 打开特定目录：

`dolphin {{path/to/directory1 path/to/directory2 ...}}`

- 打开时选择特定文件或目录：

`dolphin --select {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 打开一个新窗口：

`dolphin --new-window`

- 在分屏视图中打开特定目录：

`dolphin --split {{path/to/directory1}} {{path/to/directory2}}`

- 启动守护进程（仅在使用 D-Bus 接口时需要）：

`dolphin --daemon`

- 显示帮助：

`dolphin --help`