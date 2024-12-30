# sccmap

> 提取有向图的强连通分量。
> Graphviz 过滤器: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`。
> 更多信息: <https://www.graphviz.org/pdf/sccmap.1.pdf>。

- 提取一个或多个有向图的强连通分量：

`sccmap -S {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- 打印图的统计信息，不生成输出图：

`sccmap -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- 显示帮助信息：

`sccmap -?`