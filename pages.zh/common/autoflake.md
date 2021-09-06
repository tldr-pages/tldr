# autoflake

> 一个工具，用于检查 Python 代码中未被使用的引入和变量。
> 更多信息：<https://github.com/myint/autoflake>.

- 移除指定文件中未使用的变量，并展示 diff:

`autoflake --remove-unused-variables {{文件.py}}`

- 移除多个文件中未使用的引入，并展示 diffs:

`autoflake --remove-all-unused-imports {{文件1.py}} {{文件2.py}} {{文件3.py}}`

- 移除未被使用的变量，并覆盖更新：

`autoflake --remove-unused-variables --in-place {{文件.py}}`

- 递归地移除指定文件夹下层所有文件中未使用的变量，并覆盖更新：

`autoflake --remove-unused-variables --in-place --recursive {{路径/到/目录}}`
