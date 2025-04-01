# ippfind

> 在 DNS 服务器上查找已注册的服务或通过本地设备可用的服务。
> 参见：`ipptool`, `ippeveprinter`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-ippfind.html>。

- 列出网络上已注册的 IPP 打印机及其状态：

`ippfind --ls`

- 将特定的 PostScript 文档发送到网络上的每个 PostScript 打印机：

`ippfind --txt-pdl application/postscript --exec ipptool -f {{path/to/document.ps}} '{}' print-job.test \;`

- 将 PostScript 测试文档发送到网络上的每个 PostScript 打印机：

`ippfind --txt-pdl application/postscript --exec ipptool -f onepage-letter.ps '{}' print-job.test \;`

- 将 PostScript 测试文档发送到网络上名称匹配正则表达式的每个 PostScript 打印机：

`ippfind --txt-pdl application/postscript --host {{regex}} --exec ipptool -f onepage-letter.ps '{}' print-job.test \;`
