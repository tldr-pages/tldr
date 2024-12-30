# checkinstall

> 跟踪软件包的本地安装，并生成可以与系统本地软件包管理器一起使用的二进制软件包。
> 更多信息：<https://checkinstall.izto.org>。

- 创建并安装一个具有默认设置的软件包：

`sudo checkinstall --default`

- 创建一个软件包但不安装它：

`sudo checkinstall --install={{no}}`

- 创建一个不包含文档的软件包：

`sudo checkinstall --nodoc`

- 创建一个软件包并设置名称：

`sudo checkinstall --pkgname {{package}}`

- 创建一个软件包并指定保存位置：

`sudo checkinstall --pakdir {{path/to/directory}}`