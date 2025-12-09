# apt-clone

> 克隆/备份/恢复基于 Debian 系统的软件包状态。
> 更多信息：<https://github.com/mvo5/apt-clone>.

- 将当前系统的软件包状态克隆到指定目录：

`apt-clone clone {{路径/到/目录}}`

- 创建克隆文件（tar.gz）用于备份：

`apt-clone clone --destination {{路径/到/备份文件.tar.gz}}`

- 从克隆文件恢复软件包状态：

`apt-clone restore {{路径/到/备份文件.tar.gz}}`

- 显示克隆文件的信息（如发行版、架构等）：

`apt-clone info {{路径/到/备份文件.tar.gz}}`

- 检查克隆文件是否可以在当前系统上恢复：

`apt-clone restore {{路径/到/备份文件.tar.gz}} --destination {{路径/到/恢复目录}}`
