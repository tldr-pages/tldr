# Show-Markdown

> 在控制台中使用 VT100 转义序列或在浏览器中使用 HTML 以友好方式显示 Markdown 文件或字符串。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/show-markdown>.

- 从文件中将 Markdown 渲染到控制台：

`Show-Markdown -Path {{path\to\file}}`

- 从字符串中将 Markdown 渲染到控制台：

`"{{# Markdown 内容}}" | Show-Markdown`

- 在浏览器中打开 Markdown 文件：

`Show-Markdown -Path {{path\to\file}} -UseBrowser`