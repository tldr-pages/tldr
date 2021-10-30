# apt-cache

> Debian 和 Ubuntu 的包查询工具。
> 更多信息：<https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- 在当前的软件源中查找一个软件包：

`apt-cache search {{软件包}}`

- 显示指定软件包的相关信息：

`apt-cache show {{软件包}}`

- 查看一个软件包是否安装或是否为最新：

`apt-cache policy {{软件包}}`

- 显示一个软件包的依赖项：

`apt-cache depends {{软件包}}`

- 列出依赖指定软件包的所有软件包：

`apt-cache rdepends {{软件包}}`
