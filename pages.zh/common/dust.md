# dust

> Dust 可以快速概览哪些目录占用了磁盘空间。
> 更多信息请访问: <https://github.com/bootandy/dust>。

- 显示当前目录的信息：

`dust`

- 显示一个或多个目录的信息：

`dust {{path/to/directory1 path/to/directory2 ...}}`

- 显示30个目录（默认显示21个）：

`dust --number-of-lines 30`

- 显示当前目录的信息，深度最多为3层：

`dust --depth 3`

- 将最大的目录放在顶部，按降序排列：

`dust --reverse`

- 忽略所有具有特定名称的文件和目录：

`dust --ignore-directory {{file_or_directory_name}}`

- 不显示百分比条和百分比：

`dust --no-percent-bars`