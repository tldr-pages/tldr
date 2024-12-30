# mat2

> 通过删除元数据来匿名化各种文件格式。
> 更多信息：<https://0xacab.org/jvoisin/mat2>。

- 列出支持的文件格式：

`mat2 --list`

- 从文件中删除元数据：

`mat2 {{path/to/file}}`

- 从文件中删除元数据并将详细输出打印到控制台：

`mat2 --verbose {{path/to/file}}`

- 显示文件中的元数据而不删除它：

`mat2 --show {{path/to/file}}`

- 部分删除文件中的元数据：

`mat2 --lightweight {{path/to/file}}`

- 在原地从文件中删除元数据，而不创建备份：

`mat2 --inplace {{path/to/file}}`