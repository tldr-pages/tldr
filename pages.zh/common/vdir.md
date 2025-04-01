# vdir

> 列出目录内容。
> 作为 `ls -l` 的替代工具。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/vdir-invocation.html>。

- 列出当前目录中的文件和目录，每个条目占一行，并显示详细信息：

`vdir`

- 以人类可读的单位（KB、MB、GB）显示文件大小：

`vdir -h`

- 包括隐藏文件（以点开头的文件）：

`vdir -a`

- 按大小排序（从大到小）列出文件和目录：

`vdir -S`

- 按修改时间排序（从新到旧）列出文件和目录：

`vdir -t`

- 将目录先于文件列出：

`vdir --group-directories-first`

- 递归列出指定目录中的所有文件和目录：

`vdir --recursive {{path/to/directory}}`