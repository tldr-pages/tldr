# silicon

> 创建源代码的图像。
> 更多信息：<https://github.com/Aloxaf/silicon>.

- 从特定的源文件生成图像：

`silicon {{path/to/source_file}} --output {{path/to/output_image}}`

- 从源文件生成带有特定编程语言语法高亮的图像（例如 `rust`、`py`、`js` 等）：

`silicon {{path/to/source_file}} --output {{path/to/output_image}} --language {{language|extension}}`

- 从 `stdin` 生成图像：

`{{command}} | silicon --output {{path/to/output_image}}`