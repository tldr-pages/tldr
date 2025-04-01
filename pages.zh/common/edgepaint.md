# edgepaint

> 对图形布局的边缘进行着色，以澄清交叉边缘。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息：<https://graphviz.org/pdf/edgepaint.1.pdf>.

- 对一个或多个已经有布局信息的图形布局的边缘进行着色，以澄清交叉边缘：

`edgepaint {{路径/到/布局1.gv}} {{路径/到/布局2.gv ...}} > {{路径/到/输出.gv}}`

- 使用颜色方案对边缘进行着色。（参见：<https://graphviz.org/doc/info/colors.html#brewer>）：

`edgepaint -color-scheme={{accent7}} {{路径/到/布局.gv}} > {{路径/到/输出.gv}}`

- 对图形进行布局并对其边缘进行着色，然后将其转换为 PNG 图像：

`dot {{路径/到/输入.gv}} | edgepaint | dot -T {{png}} > {{路径/到/输出.png}}`

- 显示 `edgepaint` 的帮助信息：

`edgepaint -?`
