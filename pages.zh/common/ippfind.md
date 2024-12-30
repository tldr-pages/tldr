# ippfind

> 查找注册在DNS服务器上的服务或通过本地设备可用的服务。
> 另见：`ipptool`，`ippeveprinter`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-ippfind.html>。

- 列出网络上注册的IPP打印机及其状态：

`ippfind --ls`

- 将特定的PostScript文档发送到网络上的每台PostScript打印机：

`ippfind --txt-pdl application/postscript --exec ipptool -f {{path/to/document.ps}} '{}' print-job.test \;`

- 将PostScript测试文档发送到网络上的每台PostScript打印机：

`ippfind --txt-pdl application/postscript --exec ipptool -f onepage-letter.ps '{}' print-job.test \;`

- 将PostScript测试文档发送到网络上每台名称匹配正则表达式的PostScript打印机：

`ippfind --txt-pdl application/postscript --host {{regex}} --exec ipptool -f onepage-letter.ps '{}' print-job.test \;`