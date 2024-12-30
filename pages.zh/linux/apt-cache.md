# apt-cache

> Debian 和 Ubuntu 的软件包查询工具。
> 更多信息：<https://manned.org/apt-cache.8>。

- 在当前源中搜索软件包：

`apt-cache search {{query}}`

- 显示有关软件包的信息：

`apt-cache show {{package}}`

- 显示软件包是否已安装且是最新的：

`apt-cache policy {{package}}`

- 显示软件包的依赖关系：

`apt-cache depends {{package}}`

- 显示依赖于特定软件包的其他软件包：

`apt-cache rdepends {{package}}`