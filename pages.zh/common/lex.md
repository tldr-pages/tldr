# lex

> 词法分析器生成器。
> 根据词法分析器的规范，生成实现它的 C 代码。
> 注意：在大多数主要操作系统中，该命令是 `flex` 的别名。
> 更多信息：<https://manned.org/lex>。

- 从 Lex 文件生成分析器，存储到文件 `lex.yy.c`：

`lex {{analyzer.l}}`

- 指定输出文件：

`lex -t {{analyzer.l}} > {{analyzer.c}}`

- 编译由 Lex 生成的 C 文件：

`c99 {{path/to/lex.yy.c}} -o {{executable}}`