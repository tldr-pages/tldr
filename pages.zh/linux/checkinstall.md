# checkinstall

> 跟踪本地软件包的安装，并生成一个可以与系统的本地包管理器一起使用的二进制包。
> 更多信息：<https://checkinstall.izto.org>。

- 使用默认设置创建并安装包：

`sudo checkinstall --default`

- 创建包但不安装：

`sudo checkinstall --install={{no}}`

- 创建包但不包含文档：

`sudo checkinstall --nodoc`

- 创建包并设置名称：

`sudo checkinstall --pkgname {{package}}`

- 创建包并指定保存位置：

`sudo checkinstall --pakdir {{path/to/directory}}`