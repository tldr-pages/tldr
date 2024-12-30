# vdir

> 列出目录内容。
> `ls -l` 的替代命令。
> 更多信息：<https://www.gnu.org/software/coreutils/vdir>。

- 列出当前目录中的文件和目录，每行一个，并显示详细信息：

`vdir`

- 以人类可读的单位（KB、MB、GB）显示大小：

`vdir -h`

- 包括隐藏文件（以点开头）：

`vdir -a`

- 按大小排序列出文件和目录（最大者优先）：

`vdir -S`

- 按修改时间排序列出文件和目录（最新者优先）：

`vdir -t`

- 先列出目录：

`vdir --group-directories-first`

- 递归列出特定目录中的所有文件和目录：

`vdir --recursive {{path/to/directory}}`