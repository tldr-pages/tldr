# mingle

> 捆绑图形布局中的边缘。
> Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
> 更多信息： <https://www.graphviz.org/pdf/mingle.1.pdf>.

- 捆绑一个或多个已经有布局信息的图形布局的边缘：

`mingle {{路径/到/布局1.gv}} {{路径/到/布局2.gv ...}} > {{路径/到/输出.gv}}`

- 通过一个命令执行布局、捆绑和输出到图片：

`dot {{路径/到/输入.gv}} | mingle | dot -T {{png}} > {{路径/到/输出.png}}`

- 显示 `mingle` 的帮助信息：

`mingle -?`
