# fdp

> 从 `graphviz` 文件渲染一个 `力导向` 网络图像。
> 布局：`dot`、`neato`、`twopi`、`circo`、`fdp`、`sfdp`、`osage` 和 `patchwork`。
> 更多信息：<https://graphviz.org/doc/info/command.html>。

- 根据输入文件名和输出格式（大写 -O）渲染 PNG 图像：

`fdp -T png -O {{path/to/input.gv}}`

- 使用指定的输出文件名（小写 -o）渲染 SVG 图像：

`fdp -T svg -o {{path/to/image.svg}} {{path/to/input.gv}}`

- 以特定格式渲染输出：

`fdp -T {{ps|pdf|svg|fig|png|gif|jpg|json|dot}} -O {{path/to/input.gv}}`

- 使用 `stdin` 和 `stdout` 渲染 `gif` 图像：

`echo "{{digraph {this -> that} }}" | fdp -T gif > {{path/to/image.gif}}`

- 显示帮助：

`fdp -?`