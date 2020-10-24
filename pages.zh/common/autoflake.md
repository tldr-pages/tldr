# autoflake

> 一个工具，用于检查python代码中未被使用的引入和变量.
> 详见: <https://github.com/myint/autoflake>.

- 移除指定文件中国呢未使用的变量，并展示diff:

`autoflake --remove-unused-variables {{file.py}}`

- 移除多个文件中未使用的引入，并展示diffs:

`autoflake --remove-all-unused-imports {{file1.py}} {{file2.py}} {{file3.py}}`

- 移除未被使用的变量，并覆盖更新:

`autoflake --remove-unused-variables --in-place {{file.py}}`

- 移除指定文件夹下层所有文件（递归层级）中未使用的变量，并覆盖更新:

`autoflake --remove-unused-variables --in-place --recursive {{path/to/directory}}`
