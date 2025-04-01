# gvcolor

> 用一系列颜色为有序有向图着色。
> Graphviz 过滤器: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`。
> 更多信息：<https://graphviz.org/pdf/gvcolor.1.pdf>.

- 为一个或多个已被 `dot` 处理的有序有向图着色:

`gvcolor {{路径/到/布局1.gv}} {{路径/到/布局2.gv ...}} > {{路径/到/输出.gv}}`

- 对一个图进行布局和着色，然后将其转换为 PNG 图像:

`dot {{路径/到/输入.gv}} | gvcolor | dot -T {{png}} > {{路径/到/输出.png}}`

- 显示 `gvcolor` 的帮助信息:

`gvcolor -?`
