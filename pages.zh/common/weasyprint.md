# weasyprint

> 将HTML渲染为PDF或PNG。
> 更多信息：<https://weasyprint.org/>.

- 将HTML文件渲染为PDF：

`weasyprint {{path/to/input.html}} {{path/to/output.pdf}}`

- 将HTML文件渲染为PNG，包括一个额外的用户样式表：

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --stylesheet {{path/to/stylesheet.css}}`

- 渲染时输出额外的调试信息：

`weasyprint {{path/to/input.html}} {{path/to/output.pdf}} --verbose`

- 在输出到PNG时指定自定义分辨率：

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --resolution {{300}}`

- 为输入HTML文件中的相对URL指定基URL：

`weasyprint {{path/to/input.html}} {{path/to/output.png}} --base-url {{url_or_filename}}`