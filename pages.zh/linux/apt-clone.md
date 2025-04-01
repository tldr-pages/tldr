# apt-clone

> 克隆/备份/恢复基于 Debian 系统的软件包状态。
> 更多信息：<https://github.com/mvo5/apt-clone>。

- 将当前系统的软件包状态克隆到指定目录：

`apt-clone clone {{path/to/directory}}`

- 创建一个克隆文件（`tar.gz`）用于备份：

`apt-clone clone --destination {{path/to/backup.tar.gz}}`

- 从克隆文件中恢复软件包状态：

`apt-clone restore {{path/to/backup.tar.gz}}`

- 显示克隆文件的信息（例如发行版、架构）：

`apt-clone info {{path/to/backup.tar.gz}}`

- 检查克隆文件是否可以在当前系统上恢复：

`apt-clone restore {{path/to/backup.tar.gz}} --destination {{path/to/restore}}`
