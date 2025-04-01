# eclean

> 清理仓库源文件和二进制包。
> 更多信息：<https://wiki.gentoo.org/wiki/Eclean>.

- 清理源文件目录：

`sudo eclean distfiles`

- 清理二进制包目录：

`sudo eclean packages`

- 清理所有未安装包的 distfiles，但保留已安装包的 distfiles：

`sudo eclean --deep --package-names distfiles`

- 清理所有未安装包的二进制包，但保留已安装包的二进制包：

`sudo eclean --deep --package-names packages`
