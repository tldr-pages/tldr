# handlr

> 管理默认应用程序。
> 更多信息：<https://github.com/chmln/handlr>.

- 使用默认应用程序打开 URL：

`handlr open {{https://example.com}}`

- 使用默认 PDF 查看器打开 PDF：

`handlr open {{path/to/file.pdf}}`

- 设置 `imv` 为 PNG 文件的默认应用程序：

`handlr set {{.png}} {{imv.desktop}}`

- 设置 MPV 为所有音频文件的默认应用程序：

`handlr set {{'audio/*'}} {{mpv.desktop}}`

- 列出所有默认应用程序：

`handlr list`

- 打印 PNG 文件的默认应用程序：

`handlr get {{.png}}`