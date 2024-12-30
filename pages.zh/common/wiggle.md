# wiggle

> 一种补丁应用工具，用于解决 `patch` 无法处理的补丁冲突。
> 注意：Wiggle 强制应用所有更改，当出现冲突时进行合并，并报告无法解决的问题。
> 更多信息：<https://manned.org/wiggle>。

- 将补丁文件中的更改应用到原始文件：

`wiggle {{path/to/my_patch.patch}}`

- 将更改应用到 [o]utput 文件：

`wiggle {{path/to/my_patch.patch}} -o {{path/to/output_file.txt}}`

- 将 `file.rej` 中无法应用的任何更改合并到一个文件中：

`wiggle --replace {{path/to/file}} {{path/to/file.rej}}`

- E[x]tract 补丁或合并文件的一个分支：

`wiggle -x {{path/to/my_patch.patch}}`

- 应用补丁并将比较的单词保存到 [o]utput 文件：

`wiggle --words {{path/to/my_word_patch.patch}} -o {{path/to/word_patched_code.c}}`

- 显示有关合并功能的帮助信息：

`wiggle --merge --help`