# astyle

> C、C++、C# 和 Java 编程语言的源代码缩进器、格式化工具和美化工具。
> 运行时，会创建一个原始文件的副本，文件名后附加 ".orig"。
> 更多信息：<https://astyle.sourceforge.net>。

- 应用默认样式，缩进为 4 个空格，没有格式更改：

`astyle {{source_file}}`

- 应用带大括号的 Java 样式：

`astyle --style=java {{path/to/file}}`

- 应用带断开的括号的 Allman 样式：

`astyle --style=allman {{path/to/file}}`

- 使用空格应用自定义缩进。选择 2 到 20 个空格：

`astyle --indent=spaces={{number_of_spaces}} {{path/to/file}}`

- 使用制表符应用自定义缩进。选择 2 到 20 个制表符：

`astyle --indent=tab={{number_of_tabs}} {{path/to/file}}`