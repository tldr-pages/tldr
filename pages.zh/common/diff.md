# diff

> 比较文件和目录。
> 更多信息：<https://manned.org/diff>。

- 比较文件（列出将 `old_file` 转换为 `new_file` 的更改）：

`diff {{old_file}} {{new_file}}`

- 比较文件，忽略空白：

`diff {{-w|--ignore-all-space}} {{old_file}} {{new_file}}`

- 并排比较文件，显示差异：

`diff {{-y|--side-by-side}} {{old_file}} {{new_file}}`

- 以统一格式显示文件差异（如 `git diff` 使用的格式）：

`diff {{-u|--unified}} {{old_file}} {{new_file}}`

- 递归比较目录（显示不同文件/目录的名称以及对文件所做的更改）：

`diff {{-r|--recursive}} {{old_directory}} {{new_directory}}`

- 比较目录，仅显示不同文件的名称：

`diff {{-r|--recursive}} {{-q|--brief}} {{old_directory}} {{new_directory}}`

- 从两个文本文件的差异中为 Git 创建补丁文件，将不存在的文件视为空文件：

`diff {{-a|--text}} {{-u|--unified}} {{-N|--new-file}} {{old_file}} {{new_file}} > {{diff.patch}}`

- 比较文件，输出结果带颜色，并努力找到更小的更改集：

`diff {{-d|--minimal}} --color=always {{old_file}} {{new_file}}`