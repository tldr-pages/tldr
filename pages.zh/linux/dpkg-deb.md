# dpkg-deb

> 打包、解包并提供 Debian 归档的信息。
> 更多信息：<https://manned.org/dpkg-deb>.

- 显示包的信息：

`dpkg-deb --info {{path/to/file.deb}}`

- 在一行中显示包的名称和版本：

`dpkg-deb --show {{path/to/file.deb}}`

- 列出包的内容：

`dpkg-deb --contents {{path/to/file.deb}}`

- 将包的内容解压到一个目录中：

`dpkg-deb --extract {{path/to/file.deb}} {{path/to/directory}}`

- 从指定的目录创建一个包：

`dpkg-deb --build {{path/to/directory}}`
