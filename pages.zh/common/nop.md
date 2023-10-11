# nop

> 检查有效性并以规范的格式漂亮地打印图形。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息： <https://www.graphviz.org/pdf/nop.1.pdf>.

- 漂亮地打印一个或多个规范格式的图形：

`nop {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}} > {{路径/到/输出.gv}}`

- 检查一个或多个图形的有效性，不生成输出图形：

`nop -p {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}}`

- 显示 `nop` 的帮助信息：

`nop -?`
