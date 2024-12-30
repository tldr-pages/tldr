# tred

> 计算有向图的传递约简。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://www.graphviz.org/pdf/tred.1.pdf>。

- 构建一个或多个有向图的传递约简图：

`tred {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- 显示帮助信息：

`tred -?`