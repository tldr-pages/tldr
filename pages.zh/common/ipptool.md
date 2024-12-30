# ipptool

> 发出 IPP 请求并接收打印机/服务器的响应。
> 另请参见：`ippfind`，`ippeveprinter`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-ipptool.html>。

- 获取打印机支持的所有属性及其值：

`ipptool ipp://{{printer_uri}} get-completed-jobs.test`

- 获取打印机已完成作业的列表：

`ipptool ipp://{{printer_uri}} get-completed-jobs.test`

- 当打印机发生变化时发送电子邮件通知：

`ipptool -d recipient=mailto:{{email}} ipp://{{printer_uri}} create-printer-subscription.test`