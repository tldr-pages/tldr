# gladtex

> 一个用于 HTML 文件的 LaTeX 公式预处理器。
> 它将 LaTeX 公式转换为图像。
> 更多信息：<https://manned.org/gladtex.1>。

- 转换为 HTML：

`gladtex {{path/to/input.htex}}`

- 将转换后的文件保存到特定位置：

`gladtex {{path/to/input.htex}} -o {{path/to/output.html}}`

- 将生成的图像保存到特定[d]irectory：

`gladtex {{path/to/input.htex}} -d {{path/to/image_output_directory}}`

- 设置图像[r]esolution（以 dpi 为单位，默认值为 100）：

`gladtex {{path/to/input.htex}} -r {{resolution}}`

- 在转换后[k]eep LaTeX 文件：

`gladtex {{path/to/input.htex}} -k`

- 设置图像的[b]ackground 和[f]oreground 颜色：

`gladtex {{path/to/input.htex}} -b {{background_color}} -f {{foreground_color}}`

- 使用 `pandoc` 和 `gladtex` 将 Markdown 转换为 HTML：

`pandoc -s -t html --gladtex {{path/to/input.md}} | gladtex -o {{path/to/output.html}}`