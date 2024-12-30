# repo-add

> 软件包数据库维护工具，可通过 Pacman 安装指定软件包。
> 更多信息：<https://manned.org/repo-add>。

- 创建一个空的仓库：

`repo-add {{path/to/database.db.tar.gz}}`

- 添加当前目录中的所有软件包二进制文件并删除旧的数据库文件：

`repo-add --remove {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- 在静默模式下添加当前目录中的所有软件包二进制文件，但显示警告和错误信息：

`repo-add --quiet {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- 在不显示颜色的情况下添加当前目录中的所有软件包二进制文件：

`repo-add --nocolor {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`