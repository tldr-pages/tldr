# gv2gml

> 将图从 `gv` 格式转换为 `gml` 格式。
> 转换器：`gml2gv`、`gv2gml`、`gv2gxl`、`gxl2gv`、`graphml2gv` 和 `mm2gv`。
> 更多信息：<https://graphviz.org/pdf/gml2gv.1.pdf>。

- 将图从 `gv` 格式转换为 `gml` 格式：

`gv2gml -o {{output.gml}} {{input.gv}}`

- 使用 `stdin` 和 `stdout` 进行图的转换：

`cat {{input.gv}} | gv2gml > {{output.gml}}`

- 显示帮助信息：

`gv2gml -?`
