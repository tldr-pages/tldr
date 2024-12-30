# dpkg

> Debian 包管理器。
> 一些子命令，如 `deb`，有其自己的使用文档。
> 有关其他包管理器中的等效命令，请参见 <https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://manned.org/dpkg>。

- 安装一个包：

`dpkg -i {{path/to/file.deb}}`

- 移除一个包：

`dpkg -r {{package}}`

- 列出已安装的包：

`dpkg -l {{pattern}}`

- 列出一个包的内容：

`dpkg -L {{package}}`

- 列出本地包文件的内容：

`dpkg -c {{path/to/file.deb}}`

- 查找哪个包拥有一个文件：

`dpkg -S {{path/to/file}}`

- 清除一个已安装的或已删除的包，包括配置：

`dpkg -P {{package}}`