# autoflake

> 从 Python 代码中移除未使用的导入和变量。
> 更多信息：<https://github.com/myint/autoflake>。

- 从单个文件中移除未使用的变量并显示差异：

`autoflake --remove-unused-variables {{path/to/file.py}}`

- 从多个文件中移除未使用的导入并显示差异：

`autoflake --remove-all-unused-imports {{path/to/file1.py path/to/file2.py ...}}`

- 从文件中移除未使用的变量，覆盖该文件：

`autoflake --remove-unused-variables --in-place {{path/to/file.py}}`

- 从目录中的所有文件递归移除未使用的变量，覆盖每个文件：

`autoflake --remove-unused-variables --in-place --recursive {{path/to/directory}}`