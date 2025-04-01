# graphml2gv

> 将图表从 `graphml` 格式转换为 `gv` 格式。
> 转换工具：`gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` 和 `mm2gv`。
> 更多信息：<https://graphviz.org/pdf/graphml2gv.1.pdf>。

- 将图表从 `gml` 格式转换为 `gv` 格式：

`graphml2gv -o {{output.gv}} {{input.gml}}`

- 使用 `stdin` 和 `stdout` 转换图表：

`cat {{input.gml}} | graphml2gv > {{output.gv}}`

- 显示帮助：

`graphml2gv -?`
