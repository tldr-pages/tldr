# shiny-mirrors

> 为 Manjaro Linux 生成 `pacman` 镜像列表。
> 每次运行 shiny-mirrors 都需要您使用 `sudo pacman -Syyu` 同步数据库并更新系统。
> 更多信息：<https://gitlab.com/Arisa_Snowbell/shiny-mirrors/-/blob/domina/shiny-mirrors/man/shiny-mirrors.md>。

- 获取当前镜像的状态：

`shiny-mirrors status`

- 使用默认行为生成镜像列表：

`sudo shiny-mirrors refresh`

- 显示当前配置文件：

`shiny-mirrors config show`

- 交互式切换到不同的分支：

`sudo shiny-mirrors config --branch`