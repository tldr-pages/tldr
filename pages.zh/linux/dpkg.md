# dpkg

> Debian 软件包管理器。
> 某些子命令（如 `deb`）有自己的使用文档。
> 其他软件包管理器的等效命令，请参阅：<https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://manned.org/dpkg>。

- 安装一个软件包：

`dpkg -i {{path/to/file.deb}}`

- 删除一个软件包：

`dpkg -r {{package}}`

- 列出已安装的软件包：

`dpkg -l {{pattern}}`

- 列出一个软件包的内容：

`dpkg -L {{package}}`

- 列出本地软件包文件的内容：

`dpkg -c {{path/to/file.deb}}`

- 查找拥有某个文件的软件包：

`dpkg -S {{path/to/file}}`

- 卸载已安装或已删除的软件包，包括配置文件：

`dpkg -P {{package}}`
