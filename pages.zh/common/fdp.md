# fdp

> 从 `graphviz` 文件渲染 `force-directed` 网络图的图像。
> 布局类型：`dot`，`neato`，`twopi`，`circo`，`fdp`，`sfdp`，`osage` 和 `patchwork`。
> 更多信息：<https://graphviz.org/doc/info/command.html>。

- 渲染 PNG 图像，文件名基于输入文件名和输出格式（大写 -O）：

`fdp -T png -O {{path/to/input.gv}}`

- 渲染 SVG 图像，并指定输出文件名（小写 -o）：

`fdp -T svg -o {{path/to/image.svg}} {{path/to/input.gv}}`

- 以特定格式渲染输出：

`fdp -T {{ps|pdf|svg|fig|png|gif|jpg|json|dot}} -O {{path/to/input.gv}}`

- 使用 `stdin` 和 `stdout` 渲染 `gif` 图像：

`echo "{{digraph {this -> that} }}" | fdp -T gif > {{path/to/image.gif}}`

- 显示帮助：

`fdp -?`
