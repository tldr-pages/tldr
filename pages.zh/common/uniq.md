# uniq

> 输出输入或文件中的唯一行。
> 因为它不检测相邻的重复行，所以我们需要先对它们进行排序。
> 更多信息：<https://www.gnu.org/software/coreutils/uniq>。

- 每行显示一次：

`sort {{path/to/file}} | uniq`

- 仅显示唯一行：

`sort {{path/to/file}} | uniq -u`

- 仅显示重复行：

`sort {{path/to/file}} | uniq -d`

- 显示每行的出现次数及该行：

`sort {{path/to/file}} | uniq -c`

- 显示每行的出现次数，按出现频率排序：

`sort {{path/to/file}} | uniq -c | sort -nr`