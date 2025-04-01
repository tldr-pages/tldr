# parquet-tools

> 显示、检查和操作 Parquet 文件。
> 更多信息：<https://github.com/apache/parquet-mr>。

- 显示 Parquet 文件的内容：

`parquet-tools cat {{path/to/parquet}}`

- 显示 Parquet 文件的前几行：

`parquet-tools head {{path/to/parquet}}`

- 打印 Parquet 文件的模式：

`parquet-tools schema {{path/to/parquet}}`

- 打印 Parquet 文件的元数据：

`parquet-tools meta {{path/to/parquet}}`

- 打印 Parquet 文件的内容和元数据：

`parquet-tools dump {{path/to/parquet}}`

- 将多个 Parquet 文件合并为一个目标文件：

`parquet-tools merge {{path/to/parquet1}} {{path/to/parquet2}} {{path/to/target_parquet}}`

- 打印 Parquet 文件的行数：

`parquet-tools rowcount {{path/to/parquet}}`

- 打印 Parquet 文件的列索引和偏移索引：

`parquet-tools column-index {{path/to/parquet}}`