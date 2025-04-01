# idnits

> 检查互联网草案是否符合提交标准。
> 检查是否违反了 <https://www.ietf.org/id-info/checklist> 中列出的要求第 2.1 和 2.2 节。
> 更多信息：<https://github.com/ietf-tools/idnits>。

- 检查文件中的问题：

`idnits {{path/to/file.txt}}`

- 统计问题数量而不显示详细信息：

`idnits --nitcount {{path/to/file.txt}}`

- 显示违规行的额外信息：

`idnits --verbose {{path/to/file.txt}}`

- 使用指定年份而非当前年份：

`idnits --year {{2021}} {{path/to/file.txt}}`

- 假设文档具有指定的状态：

`idnits --doctype {{standard|informational|experimental|bcp|ps|ds}} {{path/to/file.txt}}`
