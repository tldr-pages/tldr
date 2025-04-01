# sdiff

> 比较两个文件的差异并可选地合并这两个文件。
> 更多信息：<https://manned.org/sdiff>。

- 比较两个文件：

`sdiff {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，忽略所有制表符和空白字符：

`sdiff -W {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，忽略行尾的空白字符：

`sdiff -Z {{path/to/file1}} {{path/to/file2}}`

- 以大小写不敏感的方式比较两个文件：

`sdiff -i {{path/to/file1}} {{path/to/file2}}`

- 比较并合并两个文件，将输出写入新文件：

`sdiff -o {{path/to/merged_file}} {{path/to/file1}} {{path/to/file2}}`
