# fc-list

> 列出系统上安装的可用字体。
> 更多信息：<https://manned.org/fc-list>.

- 返回系统中已安装字体的列表：

`fc-list`

- 返回具有给定名称的已安装字体的列表：

`fc-list | grep '{{DejaVu Serif}}'`

- 返回系统中已安装字体的数量：

`fc-list | wc -l`

- 返回支持指定语言（基于区域设置代码）的已安装字体列表：

`fc-list :lang={{jp}}`

- 返回包含指定 Unicode 码位字形的已安装字体列表：

`fc-list :charset={{f303}}`
