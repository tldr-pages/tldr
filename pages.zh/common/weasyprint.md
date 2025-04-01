# weasyprint

> 将 HTML 渲染为 PDF 或 PNG。
> 更多信息：<https://weasyprint.org/>。

- 将 HTML 文件渲染为 PDF：

`weasyprint {{path/to/input.html}} {{path/to/output.pdf}}`

- 将 HTML 文件渲染为 PNG，并包含一个额外的用户样式表：

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --stylesheet {{path/to/stylesheet.css}}`

- 在渲染时输出额外的调试信息：

`weasyprint {{path/to/input.html}} {{path/to/output.pdf}} --verbose`

- 指定输出 PNG 时的自定义分辨率：

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --resolution {{300}}`

- 指定输入 HTML 文件中相对 URL 的基础 URL：

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --base-url {{url_or_filename}}`
