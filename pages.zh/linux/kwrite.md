# kwrite

> KDE桌面项目的文本编辑器。
> 另见 `kate`。
> 更多信息：<https://apps.kde.org/kwrite/>。

- 打开一个文本文件：

`kwrite {{path/to/file}}`

- 打开多个文本文件：

`kwrite {{file1 file2 ...}}`

- 以特定编码打开文本文件：

`kwrite --encoding={{UTF-8}} {{path/to/file}}`

- 打开文本文件并导航到特定的行和列：

`kwrite --line {{line_number}} --column {{column_number}} {{path/to/file}}`