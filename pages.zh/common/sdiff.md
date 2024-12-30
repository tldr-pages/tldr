# sdiff

> 比较两个文件之间的差异，并可选择合并这两个文件。
> 更多信息：<https://manned.org/sdiff>。

- 比较两个文件：

`sdiff {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，忽略所有的制表符和空格：

`sdiff -W {{path/to/file1}} {{path/to/file2}}`

- 比较两个文件，忽略行末的空格：

`sdiff -Z {{path/to/file1}} {{path/to/file2}}`

- 以不区分大小写的方式比较两个文件：

`sdiff -i {{path/to/file1}} {{path/to/file2}}`

- 比较并合并，输出写入新文件：

`sdiff -o {{path/to/merged_file}} {{path/to/file1}} {{path/to/file2}}`