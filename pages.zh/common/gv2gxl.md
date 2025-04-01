# gv2gxl

> 将图从 `gv` 格式转换为 `gxl` 格式。
> 转换器：`gml2gv`、`gv2gml`、`gv2gxl`、`gxl2gv`、`graphml2gv` 与 `mm2gv`。
> 更多信息：<https://graphviz.org/pdf/gxl2gv.1.pdf>。

- 将图从 `gv` 格式转换为 `gxl` 格式：

`gv2gxl -o {{output.gxl}} {{input.gv}}`

- 使用 `stdin` 和 `stdout` 转换图：

`cat {{input.gv}} | gv2gxl > {{output.gxl}}`

- 显示帮助：

`gv2gxl -?`