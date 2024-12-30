# xe

> 对来自另一个命令或文件的每一行执行一次命令。
> 更多信息：<https://github.com/leahneukirchen/xe>。

- 对每行输入数据作为参数运行一次命令：

`{{arguments_source}} | xe {{command}}`

- 执行命令，将占位符（标记为 `{}`）的任何出现替换为输入行：

`{{arguments_source}} | xe {{command}} {} {{optional_extra_arguments}}`

- 执行一个 shell 脚本，将每 `N` 行合并为一个调用：

`echo -e 'a\nb' | xe -N{{2}} -s 'echo $2 $1'`

- 删除所有扩展名为 `.backup` 的文件：

`find . -name {{'*.backup'}} | xe rm -v`

- 并行运行最多 `max-jobs` 个进程；默认值为 1。如果 `max-jobs` 为 0，xe 将运行与 CPU 核心数量相同的进程：

`{{arguments_source}} | xe -j {{max-jobs}} {{command}}`