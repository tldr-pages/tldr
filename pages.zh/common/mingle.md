# mingle

> 捆绑图形布局的边。
> Graphviz 过滤器: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`。
> 更多信息: <https://www.graphviz.org/pdf/mingle.1.pdf>。

- 捆绑一个或多个图形布局的边（这些布局已经有布局信息）:

`mingle {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- 使用一个命令执行布局、捆绑并输出为图片:

`dot {{path/to/input.gv}} | mingle | dot -T {{png}} > {{path/to/output.png}}`

- 显示帮助信息:

`mingle -?`