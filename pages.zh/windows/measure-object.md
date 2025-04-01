# Measure-Object

> 计算对象的数值属性，以及字符串对象（如文本文件）中的字符、单词和行。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-object>.

- 计算目录中的文件和文件夹数量：

`Get-ChildItem | Measure-Object`

- 将输入管道传递给 Measure-Command（管道传递给 `Measure-Command` 的对象可以供传递给 Expression 参数的脚本块使用）：

`"One", "Two", "Three", "Four" | Set-Content -Path "{{path\to\file}}"; Get-Content "{{path\to\file}}" | Measure-Object -Character -Line -Word`
