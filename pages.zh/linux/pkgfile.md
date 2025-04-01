# pkgfile

> 在基于 Arch 的系统中搜索官方仓库中的包文件。
> 另见: `pacman files`，描述 `pacman --files` 的用法。
> 更多信息: <https://manned.org/pkgfile>.

- 同步 pkgfile 数据库:

`sudo pkgfile --update`

- 搜索拥有特定文件的包:

`pkgfile {{filename}}`

- 列出包提供的所有文件:

`pkgfile --list {{package}}`

- 列出包提供的可执行文件:

`pkgfile --list --binaries {{package}}`

- 使用不区分大小写的匹配搜索拥有特定文件的包:

`pkgfile --ignorecase {{filename}}`

- 搜索在 `bin` 或 `sbin` 目录中拥有特定文件的包:

`pkgfile --binaries {{filename}}`

- 搜索拥有特定文件的包，并显示包的版本:

`pkgfile --verbose {{filename}}`

- 在特定仓库中搜索拥有特定文件的包:

`pkgfile --repo {{repository_name}} {{filename}}`