# apt-cache

> Debian和Ubuntu的包查询工具.

- 在当前的软件源中查找一个软件包:

`apt-cache search {{query}}`

- 显示指定软件包的相关信息:

`apt-cache show {{package}}`

- 查看一个软件包是否安装或是否为最新:

`apt-cache policy {{package}}`

- 显示一个软件包的依赖项:

`apt-cache depends {{package}}`

- 列出依赖指定软件包的所有软件包:

`apt-cache rdepends {{package}}`
