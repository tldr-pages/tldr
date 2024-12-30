# pkgfile

> 在基于Arch的系统中从官方仓库搜索文件。
> 另见：`pacman files`，描述了`pacman --files`的用法。
> 更多信息：<https://manned.org/pkgfile>。

- 同步pkgfile数据库：

`sudo pkgfile --update`

- 搜索拥有特定文件的包：

`pkgfile {{filename}}`

- 列出包提供的所有文件：

`pkgfile --list {{package}}`

- 列出包提供的可执行文件：

`pkgfile --list --binaries {{package}}`

- 使用不区分大小写的匹配搜索拥有特定文件的包：

`pkgfile --ignorecase {{filename}}`

- 搜索拥有特定文件的包，文件位于`bin`或`sbin`目录中：

`pkgfile --binaries {{filename}}`

- 搜索拥有特定文件的包，并显示包版本：

`pkgfile --verbose {{filename}}`

- 在特定仓库中搜索拥有特定文件的包：

`pkgfile --repo {{repository_name}} {{filename}}`