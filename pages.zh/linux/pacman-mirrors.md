# pacman-mirrors

> 为 Manjaro Linux 生成一个 `pacman` 镜像列表。
> 每次运行 `pacman-mirrors` 之前，您需要使用 `sudo pacman -Syyu` 同步您的数据库并更新系统。
> 另请参见：`pacman`。
> 更多信息：<https://wiki.manjaro.org/index.php?title=Pacman-mirrors>。

- 使用默认设置生成镜像列表：

`sudo pacman-mirrors --fasttrack`

- 获取当前镜像的状态：

`pacman-mirrors --status`

- 显示当前分支：

`pacman-mirrors --get-branch`

- 切换到不同的分支：

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- 生成一个仅使用您所在国家的镜像的镜像列表：

`sudo pacman-mirrors --geoip`