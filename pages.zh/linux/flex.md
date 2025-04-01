# flex

> 词法分析器生成器。
> 给定一个词法分析器的规范，生成实现该分析器的 C 代码。
> 更多信息：<https://manned.org/lex.1>。

- 从 Lex 文件生成一个分析器，将其存储到文件 `lex.yy.c` 中：

`flex {{analyzer.l}}`

- 将分析器输出到 `stdout`：

`flex {{[-t|--stdout]}} {{analyzer.l}}`

- 指定输出文件：

`flex {{analyzer.l}} {{[-o|--outfile]}} {{analyzer.c}}`

- 生成批处理扫描器而不是交互式扫描器：

`flex {{[-B|--batch]}} {{analyzer.l}}`

- 编译由 Lex 生成的 C 文件：

`cc {{path/to/lex.yy.c}} -o {{executable}}`
