# pacman --deptest

> 检查每个指定的依赖项，并返回当前系统上未满足的依赖项列表。
> 另见：`pacman`。
> 更多信息：<https://manned.org/pacman.8>。

- 打印未安装的依赖项的包名称：

`pacman -T {{package1 package2 ...}}`

- 检查已安装的包是否满足给定的最低版本：

`pacman -T "{{bash>=5}}"`

- 检查是否安装了更高版本的包：

`pacman -T "{{bash>5}}"`

- 显示帮助信息：

`pacman -T --help`