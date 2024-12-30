# lex

> 词法分析器生成器。
> 根据词法分析器的规范，生成实现它的 C 代码。
> 更多信息: <https://manned.org/lex.1>。

- 从 Lex 文件生成分析器，并将其存储到文件 `lex.yy.c`：

`lex {{analyzer.l}}`

- 将分析器输出到 `stdout`：

`lex -{{-stdout|t}} {{analyzer.l}}`

- 指定输出文件：

`lex {{analyzer.l}} --outfile {{analyzer.c}}`

- 生成一个 [B]atch 扫描器，而不是交互式扫描器：

`lex -B {{analyzer.l}}`

- 编译 Lex 生成的 C 文件：

`cc {{path/to/lex.yy.c}} --output {{executable}}`