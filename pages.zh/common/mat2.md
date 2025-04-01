# mat2

> 去除文件的元数据以匿名化各种文件格式。
> 更多信息：<https://0xacab.org/jvoisin/mat2>.

- 列出支持的文件格式：

`mat2 --list`

- 去除文件的元数据：

`mat2 {{path/to/file}}`

- 去除文件的元数据并详细输出到控制台：

`mat2 --verbose {{path/to/file}}`

- 显示文件中的元数据而不删除它：

`mat2 --show {{path/to/file}}`

- 部分去除文件的元数据：

`mat2 --lightweight {{path/to/file}}`

- 在原文件位置去除元数据，不创建备份：

`mat2 --inplace {{path/to/file}}`