# yacc

> 生成一个 LALR 解析器（用 C 语言）以及一个形式语法规范文件。
> 另见：`bison`。
> 更多信息：<https://manned.org/yacc.1p>。

- 创建一个文件 `y.tab.c`，其中包含 C 解析器代码，并编译语法文件，包含所有必要的值常量声明。（常量声明文件 `y.tab.h` 仅在使用 `-d` 标志时创建）：

`yacc -d {{path/to/grammar_file.y}}`

- 编译一个包含解析器描述和由语法中的歧义生成的冲突报告的语法文件：

`yacc -d {{path/to/grammar_file.y}} -v`

- 编译一个语法文件，并用 `prefix` 替代 `y` 作为输出文件名前缀：

`yacc -d {{path/to/grammar_file.y}} -v -b {{prefix}}`