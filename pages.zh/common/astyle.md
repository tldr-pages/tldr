# astyle

> 用于 C、C++、C# 和 Java 编程语言的源代码缩进、格式化和美化工具。
> 运行后，原始文件的副本将以 ".orig" 作为后缀附加到原始文件名。
> 更多信息：<https://astyle.sourceforge.net>。

- 应用默认的 4 个空格缩进和不改变格式：

`astyle {{source_file}}`

- 应用带有附加大括号的 Java 风格：

`astyle --style=java {{path/to/file}}`

- 应用带有断开大括号的 Allman 风格：

`astyle --style=allman {{path/to/file}}`

- 应用自定义缩进，选择 2 到 20 个空格：

`astyle --indent=spaces={{number_of_spaces}} {{path/to/file}}`

- 应用自定义缩进，选择 2 到 20 个制表符：

`astyle --indent=tab={{number_of_tabs}} {{path/to/file}}`