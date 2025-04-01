# repo-add

> 用于维护软件包数据库的工具，允许通过 Pacman 安装这些软件包。
> 更多信息：<https://manned.org/repo-add>。

- 创建一个空的软件包仓库：

`repo-add {{path/to/database.db.tar.gz}}`

- 将当前目录中的所有软件包二进制文件添加到仓库，并移除旧的数据库文件：

`repo-add {{[-R|--remove]}} {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- 以静默模式（不显示警告和错误消息以外的信息）将当前目录中的所有软件包二进制文件添加到仓库：

`repo-add {{[-q|--quiet]}} {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- 不显示颜色地将当前目录中的所有软件包二进制文件添加到仓库：

`repo-add --nocolor {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`
