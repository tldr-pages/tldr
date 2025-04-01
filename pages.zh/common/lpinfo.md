# lpinfo

> 列出连接的打印机和 CUPS 打印服务器已安装的驱动程序。
> 更多信息：<https://openprinting.github.io/cups/doc/man-lpinfo.html>.

- 列出所有当前连接的打印机：

`lpinfo -v`

- 列出所有当前已安装的打印机驱动程序：

`lpinfo -m`

- 按品牌和型号搜索已安装的打印机驱动程序：

`lpinfo --make-and-model "{{printer_model}}" -m`
