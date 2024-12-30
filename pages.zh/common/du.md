# du

> 磁盘使用情况：估算和总结文件及目录的空间使用情况。
> 更多信息：<https://www.gnu.org/software/coreutils/du>。

- 列出给定单位（B/KiB/MiB）下目录及其子目录的大小：

`du -{{b|k|m}} {{path/to/directory}}`

- 以人类可读的形式列出目录及其子目录的大小（即自动选择每个大小的适当单位）：

`du -h {{path/to/directory}}`

- 显示单个目录的大小，以人类可读的单位：

`du -sh {{path/to/directory}}`

- 列出目录及其内部所有文件和目录的可读大小：

`du -ah {{path/to/directory}}`

- 列出目录及其子目录的可读大小，深度最多为 N 层：

`du -h --max-depth=N {{path/to/directory}}`

- 列出当前目录子目录中所有 `.jpg` 文件的可读大小，并在最后显示一个累积总计：

`du -ch {{*/*.jpg}}`

- 列出某个 [t]hreshold 大小以上的所有文件和目录（包括隐藏文件）（用于调查实际占用空间的内容）：

`du --all --human-readable --threshold {{1G|1024M|1048576K}} .[^.]* *`