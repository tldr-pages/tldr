# diff

> 比较文件和目录。
> 更多信息：<https://manned.org/diff>.

- 比较文件（列出将 `old_file` 转换为 `new_file` 所需的更改）：

`diff {{old_file}} {{new_file}}`

- 比较文件，忽略空白字符：

`diff {{[-w|--ignore-all-space]}} {{old_file}} {{new_file}}`

- 比较文件，显示差异的并排视图：

`diff {{[-y|--side-by-side]}} {{old_file}} {{new_file}}`

- 比较文件，显示统一格式的差异（与 `git diff` 使用的格式相同）：

`diff {{[-u|--unified]}} {{old_file}} {{new_file}}`

- 递归比较目录（显示不同文件/目录的名称以及文件的更改）：

`diff {{[-r|--recursive]}} {{old_directory}} {{new_directory}}`

- 比较目录，仅显示不同文件的名称：

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{old_directory}} {{new_directory}}`

- 从两个文本文件的差异创建一个适用于 Git 的补丁文件，将不存在的文件视为为空文件：

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{old_file}} {{new_file}} > {{diff.patch}}`

- 比较文件，以彩色显示输出并尽量找更小的差异集：

`diff {{[-d|--minimal]}} --color=always {{old_file}} {{new_file}}`