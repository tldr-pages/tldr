# a2query

> 在基于 Debian 的操作系统上查看 Apache 运行配置。
> 更多信息：<https://manpages.debian.org/latest/apache2/a2query.html>.

- 列出启用的 Apache 模块：

`sudo a2query -m`

- 查看某个模块是否已安装：

`sudo a2query -m {{模块名}}`

- 列出已启用的虚拟主机：

`sudo a2query -s`

- 显示已启用的多进程模块：

`sudo a2query -M`

- 显示 Apache 版本：

`sudo a2query -v`
