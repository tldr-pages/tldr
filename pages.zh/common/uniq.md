# uniq

> 输出输入或文件中的唯一行。
> 因为它只检测相邻的重复行，所以需要先对它们进行排序。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- 仅显示每行一次：

`sort {{路径/到/文件}} | uniq`

- 仅显示唯一的行：

`sort {{路径/到/文件}} | uniq {{[-u|--unique]}}`

- 仅显示重复的行：

`sort {{路径/到/文件}} | uniq {{[-d|--repeated]}}`

- 显示每行的出现次数及其内容：

`sort {{路径/到/文件}} | uniq {{[-c|--count]}}`

- 显示每行的出现次数，并按出现次数从高到低排序：

`sort {{路径/到/文件}} | uniq {{[-c|--count]}} | sort {{[-nr|--numeric-sort --reverse]}}`
