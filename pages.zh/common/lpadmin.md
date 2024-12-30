# lpadmin

> 配置 CUPS 打印机和类别。
> 另见：`lpoptions`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpadmin.html>。

- 设置默认打印机：

`lpadmin -d {{printer}}`

- 删除特定打印机或类别：

`lpadmin -x {{printer|class}}`

- 将打印机添加到类别：

`lpadmin -p {{printer}} -c {{class}}`

- 从类别中移除打印机：

`lpadmin -p {{printer}} -r {{class}}`