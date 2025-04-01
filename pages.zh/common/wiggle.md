# wiggle

> 一个解决 `patch` 无法处理的补丁冲突的应用工具。
> 注意：Wiggle 会强制应用所有更改，当出现冲突时进行合并，并报告无法解决的问题。
> 更多信息：<https://manned.org/wiggle>.

- 从补丁文件应用更改到原始文件：

`wiggle {{path/to/my_patch.patch}}`

- 将更改应用到输出文件：

`wiggle {{path/to/my_patch.patch}} {{[-o|--output]}} {{path/to/output_file.txt}}`

- 将 `file.rej` 中无法应用的任何更改合并到文件中：

`wiggle {{[-r|--replace]}} {{path/to/file}} {{path/to/file.rej}}`

- 提取补丁或合并文件的一个分支：

`wiggle {{[-x|--extract]}} {{path/to/my_patch.patch}}`

- 应用补丁并将比较的单词保存到输出文件：

`wiggle {{[-w|--words]}} {{path/to/my_word_patch.patch}} {{[-o|--output]}} {{path/to/word_patched_code.c}}`

- 显示关于合并功能的帮助：

`wiggle {{[-m|--merge]}} {{[-h|--help]}}`
