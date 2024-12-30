# gvcolor

> 使用一系列颜色为有序有向图上色。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/gvcolor.1.pdf>。

- 为一个或多个已经由 `dot` 处理的有序有向图上色：

`gvcolor {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- 布局一个图并为其上色，然后转换为 PNG 图像：

`dot {{path/to/input.gv}} | gvcolor | dot -T {{png}} > {{path/to/output.png}}`

- 显示帮助信息：

`gvcolor -?`