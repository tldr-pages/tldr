# unflatten

> 调整有向图以改善布局纵横比。
> Graphviz 过滤器: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, 和 `unflatten`。
> 更多信息: <https://www.graphviz.org/pdf/unflatten.1.pdf>。

- 调整一个或多个有向图以改善布局纵横比：

`unflatten {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- 将 `unflatten` 用作 `dot` 布局的预处理器，以改善纵横比：

`unflatten {{path/to/input.gv}} | dot -T {{png}} {{path/to/output.png}}`

- 显示帮助信息：

`unflatten -?`