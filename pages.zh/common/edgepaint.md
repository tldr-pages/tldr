# edgepaint

> 为图形布局的边缘上色，以澄清交叉边。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/edgepaint.1.pdf>。

- 为一个或多个图形布局（已经具有布局信息）上色，以澄清交叉边：

`edgepaint {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- 使用颜色方案为边缘上色。（请参阅 <https://graphviz.org/doc/info/colors.html#brewer>）：

`edgepaint -color-scheme={{accent7}} {{path/to/layout.gv}} > {{path/to/output.gv}}`

- 布局一个图形并为其边缘上色，然后转换为 PNG 图像：

`dot {{path/to/input.gv}} | edgepaint | dot -T {{png}} > {{path/to/output.png}}`

- 显示帮助信息：

`edgepaint -?`