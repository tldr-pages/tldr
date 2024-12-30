# gvpack

> 组合多个图布局（已具有布局信息）。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/gvpack.1.pdf>。

- 组合多个图布局（已具有布局信息）：

`gvpack {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- 在图级别组合多个图布局，保持图的独立性：

`gvpack -g {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- 在节点级别组合多个图布局，忽略簇：

`gvpack -n {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- 组合多个图布局而不进行打包：

`gvpack -u {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- 显示帮助信息：

`gvpack -?`