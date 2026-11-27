# dust

> 概览哪些目录占用了磁盘空间。
> 另请参阅：`du`, `ncdu`。
> 更多信息：<https://github.com/bootandy/dust#usage>。

- 显示当前目录的信息：

`dust`

- 显示一个或多个目录的信息：

`dust {{路径/到/目录1 路径/到/目录2 ...}}`

- 显示 30 个目录（默认 21 个）：

`dust {{[-n|--number-of-lines]}} 30`

- 显示当前目录的信息，最多 3 层：

`dust {{[-d|--depth]}} 3`

- 按降序在最上方显示占用最多的目录：

`dust {{[-r|--reverse]}}`

- 忽略某个文件或目录：

`dust {{[-X|--ignore-directory]}} {{路径/到/文件或目录}}`

- 不显示百分比条和百分比：

`dust {{[-b|--no-percent-bars]}}`
