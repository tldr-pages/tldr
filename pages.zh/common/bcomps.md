# bcomps

> 将图分解为其双连通分量。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/bcomps.1.pdf>。

- 将一个或多个图分解为其双连通分量：

`bcomps {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- 打印一个或多个图中的块和切割顶点的数量：

`bcomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- 根据 `output.gv` 将每个块和块-切割顶点树写入多个编号的文件名：

`bcomps -x -o {{path/to/output.gv}} {{path/to/input1.gv path/to/input2.gv ...}}`

- 显示帮助信息：

`bcomps -?`