# pacman --database

> 操作 Arch Linux 软件包数据库。
> 修改已安装软件包的某些属性。
> 参见：`pacman`。
> 更多信息：<https://manned.org/pacman.8>。

- 将软件包标记为隐式安装：

`sudo pacman -D --asdeps {{package}}`

- 将软件包标记为显式安装：

`sudo pacman -D --asexplicit {{package}}`

- 检查所有软件包依赖是否已安装：

`pacman -Dk`

- 检查同步数据库以确保所有可下载软件包的指定依赖项均可用：

`pacman -Dkk`

- 检查并以安静模式显示（仅显示错误信息）：

`pacman -Dkq`

- 显示帮助：

`pacman -Dh`