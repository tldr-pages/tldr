# ccomps

> 将图形分解为它们的连通分量。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/ccomps.1.pdf>.

- 将一个或多个图形分解为它们的连通分量：

`ccomps {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}} > {{路径/到/输出.gv}}`

- 打印一个或多个图形中的节点、边和连通分量的数量：

`ccomps -v -s {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}}`

- 根据 `输出.gv` 将每个连通分量写入多个有编号的文件中：

`ccomps -x -o {{路径/到/输出.gv}} {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}}`

- 显示 `ccomps` 的帮助信息：

`ccomps -?`
