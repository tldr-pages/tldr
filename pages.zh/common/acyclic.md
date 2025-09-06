# acyclic

> 通过反转一些边来使有向图无环。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/acyclic.1.pdf>.

- 通过反转一些边来使有向图无环：

`acyclic {{路径/到/输入.gv}} > {{路径/到/输出.gv}}`

- 打印出一个图是无环的、有环的还是无向的，不产生输出图：

`acyclic -v -n {{路径/到/输入.gv}}`

- 显示 `acyclic` 的帮助：

`acyclic -?`
