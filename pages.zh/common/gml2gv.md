# gml2gv

> 将图形从 `gml` 格式转换为 `gv` 格式。
> 转换器：`gml2gv`、`gv2gml`、`gv2gxl`、`gxl2gv`、`graphml2gv` 和 `mm2gv`。
> 更多信息：<https://graphviz.org/pdf/gml2gv.1.pdf>。

- 将图形从 `gml` 格式转换为 `gv` 格式：

`gml2gv -o {{output.gv}} {{input.gml}}`

- 使用 `stdin` 和 `stdout` 转换图形：

`cat {{input.gml}} | gml2gv > {{output.gv}}`

- 显示帮助信息：

`gml2gv -?`