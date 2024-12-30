# ccomps

> 将图分解为其连通分量。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/ccomps.1.pdf>。

- 将一个或多个图分解为其连通分量：

`ccomps {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- 打印一个或多个图中的节点、边和连通分量的数量：

`ccomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- 将每个连通分量写入基于 `output.gv` 的编号文件名：

`ccomps -x -o {{path/to/output.gv}} {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- 显示帮助信息：

`ccomps -?`