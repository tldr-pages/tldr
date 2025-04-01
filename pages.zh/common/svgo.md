# svgo

> SVG 优化器：用于优化可缩放矢量图形文件，基于 Node.js。
> 它应用一系列可单独切换的转换规则（插件）。
> 更多信息：<https://github.com/svg/svgo>.

- 使用默认插件优化文件（覆盖原始文件）：

`svgo {{test.svg}}`

- 优化文件并将结果保存到另一个文件中：

`svgo {{test.svg}} -o {{test.min.svg}}`

- 优化目录中的所有 SVG 文件（覆盖原始文件）：

`svgo -f {{path/to/directory/with/svg/files}}`

- 优化目录中的所有 SVG 文件并将结果文件保存到另一个目录中：

`svgo -f {{path/to/input/directory}} -o {{path/to/output/directory}}`

- 从其他命令传递的 SVG 内容进行优化，并将结果保存到文件中：

`{{cat test.svg}} | svgo -i - -o {{test.min.svg}}`

- 优化文件并打印结果：

`svgo {{test.svg}} -o -`

- 显示可用插件：

`svgo --show-plugins`