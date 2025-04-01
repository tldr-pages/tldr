# dust

> Dust 可以立即提供哪些目录占用了磁盘空间的概览。
> 更多信息：<https://github.com/bootandy/dust>。

- 显示当前目录的信息：

`dust`

- 显示一个或多个目录的信息：

`dust {{path/to/directory1 path/to/directory2 ...}}`

- 显示 30 个目录（默认为 21 个）：

`dust --number-of-lines 30`

- 显示当前目录下最多 3 层深度的信息：

`dust --depth 3`

- 按降序显示最大的目录在顶部：

`dust --reverse`

- 忽略所有具有特定名称的文件和目录：

`dust --ignore-directory {{file_or_directory_name}}`

- 不显示百分比条和百分比：

`dust --no-percent-bars`