# dua

> Dua (磁盘使用分析器): 获取目录的磁盘空间使用情况。
> 更多信息: <https://github.com/Byron/dua-cli>.

- 分析特定目录：

`dua {{path/to/directory}}`

- 显示实际大小而不是磁盘使用情况：

`dua --apparent-size`

- 每次遇到硬链接文件时都进行计数：

`dua --count-hard-links`

- 聚合一个或多个目录或文件的已使用空间：

`dua aggregate`

- 启动终端用户界面：

`dua interactive`

- 格式化打印字节数：

`dua --format {{metric|binary|bytes|GB|GiB|MB|MiB}}`

- 使用特定数量的线程（默认为进程的线程数）：

`dua --threads {{count}}`
