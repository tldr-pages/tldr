# for

> 执行多次命令。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- 遍历命令行参数：

`for {{variable}}; do {{echo $variable}}; done`

- 遍历指定的每个项目：

`for {{variable}} in {{item1 item2 ...}}; do {{echo "循环被执行"}}; done`

- 遍历指定范围的数字：

`for {{variable}} in {{{from}}..{{to}}..{{step}}}; do {{echo "循环被执行"}}; done`

- 遍历指定的文件列表：

`for {{variable}} in {{path/to/file1 path/to/file2 ...}}; do {{echo "循环被执行"}}; done`

- 遍历指定的目录列表：

`for {{variable}} in {{path/to/directory1/ path/to/directory2/ ...}}; do {{echo "循环被执行"}}; done`

- 在每个目录中执行给定的命令：

`for {{variable}} in */; do (cd "${{variable}}" || continue; {{echo "循环被执行"}}) done`
