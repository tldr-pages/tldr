# twopi

> 从 `graphviz` 文件渲染一个 `radial` 网络图像。
> 布局选项：`dot`、`neato`、`twopi`、`circo`、`fdp`、`sfdp`、`osage` 和 `patchwork`。
> 更多信息：<https://graphviz.org/doc/info/command.html>。

- 使用基于输入文件名和输出格式（大写 -O）生成 PNG 图像：

`twopi -T {{png}} -O {{path/to/input.gv}}`

- 使用指定的输出文件名（小写 -o）生成 SVG 图像：

`twopi -T {{svg}} -o {{path/to/image.svg}} {{path/to/input.gv}}`

- 以 PS、PDF、SVG、Fig、PNG、GIF、JPEG、JSON 或 DOT 格式输出：

`twopi -T {{format}} -O {{path/to/input.gv}}`

- 使用 `stdin` 和 `stdout` 渲染 GIF 图像：

`echo "{{digraph {this -> that} }}" | twopi -T {{gif}} > {{path/to/image.gif}}`

- 显示帮助信息：

`twopi -?`