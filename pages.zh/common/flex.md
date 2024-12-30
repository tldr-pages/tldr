# flex

> 词法分析器生成器。对 `lex` 的重写，并扩展了 POSIX 规范。
> 根据词法分析器的规范，生成实现它的 C 代码。
> 注意：在 OpenBSD 上，长选项无效。
> 更多信息：<https://manned.org/flex>。

- 从 flex 文件生成分析器，并将其存储到文件 `lex.yy.c` 中：

`lex {{analyzer.l}}`

- 将分析器写入 `stdout`：

`lex -{{-stdout|t}} {{analyzer.l}}`

- 指定输出文件：

`lex {{analyzer.l}} -o {{analyzer.c}}`

- 生成 [B]atch 扫描器，而不是交互式扫描器：

`lex -B {{analyzer.l}}`

- 编译由 Lex 生成的 C 文件：

`cc {{path/to/lex.yy.c}} --output {{executable}}`