# for

> 多次执行一个命令。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>。

- 迭代命令行参数：

`for {{variable}}; do {{echo $variable}}; done`

- 对每个指定的项目执行给定的命令：

`for {{variable}} in {{item1 item2 ...}}; do {{echo "循环已执行"}}; done`

- 在给定的数字范围内迭代：

`for {{variable}} in {{{from}}..{{to}}..{{step}}}; do {{echo "循环已执行"}}; done`

- 在给定的文件列表中迭代：

`for {{variable}} in {{path/to/file1 path/to/file2 ...}}; do {{echo "循环已执行"}}; done`

- 在给定的目录列表中迭代：

`for {{variable}} in {{path/to/directory1/ path/to/directory2/ ...}}; do {{echo "循环已执行"}}; done`

- 在每个目录中执行给定命令：

`for {{variable}} in */; do (cd "${{variable}}" || continue; {{echo "循环已执行"}}) done`