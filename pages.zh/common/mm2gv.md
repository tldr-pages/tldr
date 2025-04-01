# mm2gv

> 将图从 Matrix Market `mm` 格式转换为 `gv` 格式。
> 转换器：`gml2gv`、`gv2gml`、`gv2gxl`、`gxl2gv`、`graphml2gv` 和 `mm2gv`。
> 更多信息：<https://graphviz.org/pdf/mm2gv.1.pdf>。

- 将图从 `mm` 转换为 `gv` 格式：

`mm2gv -o {{output.gv}} {{input.mm}}`

- 使用 `stdin` 和 `stdout` 转换图：

`cat {{input.mm}} | mm2gv > {{output.gv}}`

- 显示帮助：

`mm2gv -?`
