# nop

> 检查图的有效性并以标准格式美观地打印。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://www.graphviz.org/pdf/nop.1.pdf>。

- 以标准格式美观地打印一个或多个图：

`nop {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- 检查一个或多个图的有效性，不生成输出图：

`nop -p {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- 显示帮助信息：

`nop -?`