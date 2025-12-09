# sccmap

> 提取有向图的强连通分量。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://www.graphviz.org/pdf/sccmap.1.pdf>.

- 从一个或多个有向图中提取强连通分量：

`sccmap -S {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}} > {{路径/到/输出.gv}}`

- 打印一个图形的统计信息，不生成输出图形：

`sccmap -v -s {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}}`

- 显示 `sccmap` 的帮助信息：

`sccmap -?`
