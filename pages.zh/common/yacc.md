# yacc

> 使用形式语法规范文件生成一个 LALR 解析器（使用 C 语言）。
> 请参阅：`bison`。
> 更多信息：<https://manned.org/yacc.1p>.

- 创建一个包含 C 语言解析器代码的文件 `y.tab.c`，并编译语法文件以及所有值所需的常量声明。（只有在使用 `-d` 选项时，才会创建常量声明文件 `y.tab.h`）：

`yacc -d {{路径/到/grammar_file.y}}`

- 编译一个包含解析器描述的语法文件，以及报告由于语法中的歧义导致的冲突：

`yacc -d {{路径/到/grammar_file.y}} -v`

- 编译一个语法文件，并用 `prefix` 代替 `y` 作为输出文件名前缀：

`yacc -d {{路径/到/grammar_file.y}} -v -b {{前缀}}`
