# lpoptions

> 显示或设置打印机选项和默认值。
> 另见：`lpadmin`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpoptions.html>。

- 设置默认打印机：

`lpoptions -d {{printer[/instance]}}`

- 列出特定打印机的打印机特定选项：

`lpoptions -d {{printer}} -l`

- 在特定打印机上设置新选项：

`lpoptions -d {{printer}} -o {{option}}`

- 移除特定打印机的选项：

`lpoptions -d {{printer}} -x`