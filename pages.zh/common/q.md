# q

> 在CSV和TSV文件上执行类似SQL的查询。
> 更多信息：<https://harelba.github.io/q>。

- 通过指定分隔符为','查询CSV文件：

`q -d',' "SELECT * from {{path/to/file}}"`

- 查询TSV文件：

`q -t "SELECT * from {{path/to/file}}"`

- 查询带有表头行的文件：

`q -d{{delimiter}} -H "SELECT * from {{path/to/file}}"`

- 从`stdin`读取数据；查询中的'-'代表来自`stdin`的数据：

`{{output}} | q "select * from -"`

- 在列`c1`（一个公共列）上连接两个文件（在示例中别名为`f1`和`f2`）：

`q "SELECT * FROM {{path/to/file}} f1 JOIN {{path/to/other_file}} f2 ON (f1.c1 = f2.c1)"`

- 使用输出分隔符和输出表头行格式化输出（注意：命令将根据输入文件的表头或在查询中重写的列别名输出列名）：

`q -D{{delimiter}} -O "SELECT {{column}} as {{alias}} from {{path/to/file}}"`