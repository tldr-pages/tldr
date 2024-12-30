# idnits

> 检查互联网草案的提交小问题。
> 查找违反 <https://www.ietf.org/id-info/checklist> 上列出的要求第2.1和2.2节的情况。
> 更多信息：<https://github.com/ietf-tools/idnits>。

- 检查文件中的小问题：

`idnits {{path/to/file.txt}}`

- 统计小问题而不显示它们：

`idnits --nitcount {{path/to/file.txt}}`

- 显示有关有问题行的额外信息：

`idnits --verbose {{path/to/file.txt}}`

- 在样板中期待指定的年份，而不是当前年份：

`idnits --year {{2021}} {{path/to/file.txt}}`

- 假定文档为指定状态：

`idnits --doctype {{standard|informational|experimental|bcp|ps|ds}} {{path/to/file.txt}}`