# pkginfo

> 查询 CRUX 系统的软件包数据库。
> 更多信息：<https://crux.nu/Main/Handbook3-6#ntoc19>.

- 列出已安装的软件包及其版本：

`pkginfo -i`

- 列出指定软件包包含的文件：

`pkginfo -l {{package}}`

- 列出匹配模式的文件的所有者：

`pkginfo -o {{pattern}}`

- 打印文件的足迹：

`pkginfo -f {{path/to/file}}`