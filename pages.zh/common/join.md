# join

> 在一个公共字段上连接两个已排序文件的行。
> 更多信息：<https://www.gnu.org/software/coreutils/join>。

- 在第一个（默认）字段上连接两个文件：

`join {{path/to/file1}} {{path/to/file2}}`

- 使用逗号（而不是空格）作为字段分隔符连接两个文件：

`join -t {{','}} {{path/to/file1}} {{path/to/file2}}`

- 将file1的field3与file2的field1连接：

`join -1 {{3}} -2 {{1}} {{path/to/file1}} {{path/to/file2}}`

- 为file1中每个无法配对的行生成一行：

`join -a {{1}} {{path/to/file1}} {{path/to/file2}}`

- 从`stdin`连接一个文件：

`cat {{path/to/file1}} | join - {{path/to/file2}}`