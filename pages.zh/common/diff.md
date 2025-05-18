# diff

> 比较文件或目录。
> 更多信息: <https：//manned.org/diff>.

- 比较文件 （列出从`原文件`到`新文件`的修改）：

`diff {{原文件}} {{新文件}}`

- 比较文件，忽视空白字符

`diff {{[-w|--ignore-all-space]}} {{原文件}} {{新文件}}`

- 比较文件，并排展示文件差异：

`diff {{[-y|--side-by-side]}} {{原文件}} {{新文件}}`

- 比较文件，以统一形式展示不同区别 （ 形式同 `git diff`）：

`diff {{[-u|--unified]}} {{源文件}} {{新文件}}`

- 递归地比较目录 （展示不同文件和目录的名字和差异）：

`diff {{[-r|--recursive]}} {{old_directory}} {{new_directory}}`

- 比较目录（只展示不同文件的文件名）：

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{old_directory}} {{new_directory}}`

- 根据两个文本文件的差异，为 Git 创建补丁文件，不存在的文件会被视为空文件：

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{原文件}} {{新文件}} > {{diff.patch}}`

- 比较文件，打印彩色的输出，并尽可能找出最小的改变：

`diff {{[-d|--minimal]}} --color=always {{原文件}} {{新文件}}`
