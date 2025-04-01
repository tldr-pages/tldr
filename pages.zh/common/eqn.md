# eqn

> groff (GNU Troff) 文档格式系统的方程预处理器。
> 参见 `troff` 和 `groff`。
> 更多信息：<https://manned.org/eqn>。

- 处理包含方程的输入文件，并保存输出以供后续使用 groff 转换为 PostScript：

`eqn {{path/to/input.eqn}} > {{path/to/output.roff}}`

- 使用 [me] 宏包将包含方程的输入文件排版成 PDF：

`eqn -T {{pdf}} {{path/to/input.eqn}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`