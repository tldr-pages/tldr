# dpkg-query

> 显示已安装软件包的信息。
> 更多信息：<https://manned.org/dpkg-query.1>。

- 列出所有已安装的软件包：

`dpkg-query --list`

- 列出与指定模式匹配的已安装软件包：

`dpkg-query --list '{{libc6*}}'`

- 列出指定软件包安装的所有文件：

`dpkg-query --listfiles {{libc6}}`

- 显示软件包的详细信息：

`dpkg-query --status {{libc6}}`

- 搜索拥有与指定模式匹配的文件的软件包：

`dpkg-query --search {{/etc/ld.so.conf.d}}`
