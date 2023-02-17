# unflatten

> 调整有向图以改善布局的纵横比。
> Graphviz 过滤器: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, 和 `unflatten`。
> 更多信息: <https://www.graphviz.org/pdf/unflatten.1.pdf>.

- 调整一个或多个有向图以改善布局的纵横比:

`unflatten {{路径/到/输入1.gv}} {{路径/到/输入2.gv ...}} > {{路径/到/输出.gv}}`

- 将 `unflatten` 作为 `dot` 布局的预处理器以改善纵横比:

`unflatten {{路径/到/输入.gv}} | dot -T {{png}} {{路径/到/输出.png}}`

- 显示 `unflatten` 的帮助:

`unflatten -?`
