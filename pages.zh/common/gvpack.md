# gvpack

> 将多个具有布局信息的图形布局组合在一起。
> Graphviz 过滤器: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred` 和 `unflatten`。
> 更多信息: <https://graphviz.org/pdf/gvpack.1.pdf>.

- 将多个具有布局信息的图形布局组合在一起：

`gvpack {{路径/到/布局1.gv}} {{路径/到/布局2.gv ...}} > {{路径/到/输出.gv}}`

- 在图形层面上将多个图形布局组合在一起，保持图形分开：

`gvpack -g {{路径/到/布局1.gv}} {{路径/到/布局2.gv ...}} > {{路径/到/输出.gv}}`

- 在节点层面上将多个图形布局组合在一起，忽略簇：

`gvpack -n {{路径/到/布局1.gv}} {{路径/到/布局2.gv ...}} > {{路径/到/输出.gv}}`

- 将多个图形布局组合在一起而不进行打包：

`gvpack -u {{路径/到/布局1.gv}} {{路径/到/布局2.gv ...}} > {{路径/到/输出.gv}}`

- 显示 `gvpack` 的帮助信息：

`gvpack -?`
