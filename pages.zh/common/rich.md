# rich

> 一个用于终端中华丽输出的工具箱。
> 更多信息：<https://github.com/Textualize/rich-cli>。

- 以语法高亮显示文件：

`rich {{path/to/file.py}}`

- 添加行号和缩进指示：

`rich {{path/to/file.py}} --line-numbers --guides`

- 应用主题：

`rich {{path/to/file.py}} --theme {{monokai}}`

- 在交互式分页器中显示文件：

`rich {{path/to/file.py}} --pager`

- 从 URL 显示内容：

`rich {{https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md}} --markdown --pager`

- 将文件导出为 HTML：

`rich {{path/to/file.md}} --export-html {{path/to/file.html}}`

- 以格式标签、自定义对齐和行宽显示文本：

`rich --print "{{Hello [green on black]Stylized[/green on black] [bold]World[/bold]}}" --{{left|center|right}} --width {{10}}`