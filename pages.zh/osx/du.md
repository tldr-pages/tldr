# du

> 磁盘使用情况：估算和总结文件及目录的空间使用情况。
> 更多信息：<https://keith.github.io/xcode-man-pages/du.1.html>。

- 列出给定单位（KiB/MiB/GiB）下的目录及其任何子目录的大小：

`du -{{k|m|g}} {{path/to/directory}}`

- 以人类可读的形式列出目录及其任何子目录的大小（即自动选择每个大小的适当单位）：

`du -h {{path/to/directory}}`

- 显示单个目录的大小，以人类可读的单位表示：

`du -sh {{path/to/directory}}`

- 列出目录及其所有文件和目录内的人类可读大小：

`du -ah {{path/to/directory}}`

- 列出目录及其任何子目录的人类可读大小，最多深入 N 层：

`du -h -d {{2}} {{path/to/directory}}`

- 列出当前目录子目录中所有 `.jpg` 文件的人类可读大小，并在最后显示累积总和：

`du -ch {{*/*.jpg}}`