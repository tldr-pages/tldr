# du

> 磁盘使用率：估计和汇总文件和目录空间使用率。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html>.

- 以给定单位（B/KiB/MiB）列出目录和所有子目录的大小：

`du -{{b|k|m}} {{路径/到/目录}}`

- 以可读形式列出目录和任何子目录的大小（即自动转换为的合适的单位）：

`du {{[-h|--human-readable]}} {{路径/到/目录}}`

- 以可读单位显示目录大小：

`du {{[-sh|--summarize --human-readable]}} {{路径/到/目录}}`

- 列出目录以及其中所有文件和目录的可读大小：

`du {{[-ah|--all --human-readable]}} {{路径/到/目录}}`

- 列出目录和任何子目录的可读大小，最多可达 N 级：

`du {{[-h|--human-readable]}} {{[-d|--max-depth]}} N {{路径/到/目录}}`

- 列出当前目录中所有 `.jpg` 文件的可读大小，并在最后显示累计总数：

`du {{[-ch|--total --human-readable]}} {{./*.jpg}}`

- 列出超过特定大小的所有文件和目录（包括隐藏的文件和目录）（对于查询实际占用空间很有用）：

`du {{[-ah|--all --human-readable]}} {{[-t|--threshold]}} {{1G|1024M|1048576K}} .[^.]* *`
