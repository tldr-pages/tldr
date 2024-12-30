# handlr

> 管理您的默认应用程序。
> 更多信息：<https://github.com/chmln/handlr>。

- 在默认应用程序中打开一个 URL：

`handlr open {{https://example.com}}`

- 在默认 PDF 查看器中打开一个 PDF 文件：

`handlr open {{path/to/file.pdf}}`

- 将 `imv` 设置为 PNG 文件的默认应用程序：

`handlr set {{.png}} {{imv.desktop}}`

- 将 MPV 设置为所有音频文件的默认应用程序：

`handlr set {{'audio/*'}} {{mpv.desktop}}`

- 列出所有默认应用程序：

`handlr list`

- 打印 PNG 文件的默认应用程序：

`handlr get {{.png}}`