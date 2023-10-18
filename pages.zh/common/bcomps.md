# bcomps

> 将图形分解为它们的双连通分量。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/bcomps.1.pdf>.

- 将一个或多个图形分解为它们的双连通分量：

`bcomps {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}} > {{路径/到/输出.gv}}`

- 打印一个或多个图形中的块和切割顶点的数量：

`bcomps -v -s {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}}`

- 根据 `输出.gv` 将每个块和块切割顶点树写入多个有编号的文件中：

`bcomps -x -o {{路径/到/输出.gv}} {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}}`

- 显示 `bcomps` 的帮助信息：

`bcomps -?`
