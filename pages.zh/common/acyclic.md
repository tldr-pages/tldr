# 无环

> 通过反转一些边，使有向图无环。
> Graphviz 过滤器：`acyclic`，`bcomps`，`comps`，`edgepaint`，`gvcolor`，`gvpack`，`mingle`，`nop`，`sccmap`，`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/acyclic.1.pdf>。

- 通过反转一些边，使有向图无环：

`acyclic {{path/to/input.gv}} > {{path/to/output.gv}}`

- 打印图是否无环、是否有环或是无向图，不产生输出图：

`acyclic -v -n {{path/to/input.gv}}`

- 显示帮助信息：

`acyclic -?`