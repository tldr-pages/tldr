# Show-Markdown

> 以友好的方式在控制台中显示Markdown文件或字符串，使用VT100转义序列，或在浏览器中使用HTML。
> 注意：此命令只能通过PowerShell使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/show-markdown>。

- 从文件渲染Markdown到控制台：

`Show-Markdown -Path {{path\to\file}}`

- 从字符串渲染Markdown到控制台：

`"{{# Markdown content}}" | Show-Markdown`

- 在浏览器中打开Markdown文件：

`Show-Markdown -Path {{path\to\file}} -UseBrowser`