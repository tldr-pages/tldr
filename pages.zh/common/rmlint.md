# rmlint

> 在你的文件系统中查找空间浪费和其他损坏的文件。
> 更多信息：<https://rmlint.readthedocs.io/en/latest/rmlint.1.html>。

- 检查目录中的重复、空和损坏的文件：

`rmlint {{path/to/directory1 path/to/directory2 ...}}`

- 检查空间浪费，最好将文件保留在标记的目录中（在双斜杠之后）：

`rmlint {{path/to/directory}} // {{path/to/original_directory}}`

- 检查空间浪费，保留所有未标记的目录中的文件：

`rmlint --keep-all-untagged {{path/to/directory}} // {{path/to/original_directory}}`

- 删除通过一次执行`rmlint`找到的重复文件：

`./rmlint.sh`

- 查找重复的目录树：

`rmlint --merge-directories {{path/to/directory}}`

- 将路径较低的文件标记为原始文件，在平局时选择较短的长度：

`rmlint --rank-by={{dl}} {{path/to/directory}}`

- 仅查找具有相同文件名的重复文件，此外还要有相同的内容：

`rmlint --match-basename {{path/to/directory}}`

- 仅查找具有相同扩展名的重复文件，此外还要有相同的内容：

`rmlint --match-extension {{path/to/directory}}`