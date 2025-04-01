# lpadmin

> 配置 CUPS 打印机和打印机组。
> 参见：`lpoptions`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpadmin.html>。

- 设置默认打印机：

`lpadmin -d {{printer}}`

- 删除特定的打印机或打印机组：

`lpadmin -x {{printer|class}}`

- 将打印机添加到打印机组：

`lpadmin -p {{printer}} -c {{class}}`

- 从打印机组中移除打印机：

`lpadmin -p {{printer}} -r {{class}}`
