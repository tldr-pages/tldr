# pacman-mirrors

> 为 Manjaro Linux 生成 `pacman` 镜像列表。
> 每次运行 `pacman-mirrors` 后，都需要使用 `sudo pacman -Syyu` 同步数据库并更新系统。
> 参见: `pacman`。
> 更多信息: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>。

- 使用默认设置生成镜像列表：

`sudo pacman-mirrors --fasttrack`

- 获取当前镜像的状态：

`pacman-mirrors --status`

- 显示当前的分支：

`pacman-mirrors --get-branch`

- 切换到不同的分支：

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- 生成仅使用本国镜像的镜像列表：

`sudo pacman-mirrors --geoip`
