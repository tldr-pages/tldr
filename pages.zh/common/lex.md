# lex

> 词法分析器生成器。
> 根据词法分析器的规范，生成实现它的C代码。
> 注意：在大多数主要操作系统上，此命令是`flex`的别名。
> 更多信息：<https://manned.org/lex.1>。

- 从Lex文件生成分析器，并将其存储到文件`lex.yy.c`中：

`lex {{analyzer.l}}`

- 指定输出文件：

`lex -t {{analyzer.l}} > {{analyzer.c}}`

- 编译由Lex生成的C文件：

`c99 {{path/to/lex.yy.c}} -o {{executable}}`