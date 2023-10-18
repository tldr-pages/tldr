# tred

> 计算有向图的传递闭包约简。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息： <https://www.graphviz.org/pdf/tred.1.pdf>.

- 构建一个或多个有向图的传递闭包约简：

`tred {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}} > {{路径/到/输出.gv}}`

- 显示帮助信息：

`tred -?`
