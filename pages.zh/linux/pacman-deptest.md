# pacman --deptest

> 检查每个指定的依赖项，并返回系统上未满足的依赖项列表。
> 参见: `pacman`。
> 更多信息: <https://manned.org/pacman.8>。

- 打印未安装的依赖项的包名：

`pacman -T {{package1 package2 ...}}`

- 检查是否安装了满足给定最小版本的包：

`pacman -T "{{bash>=5}}"`

- 检查是否安装了大于指定版本的包：

`pacman -T "{{bash>5}}"`

- 显示帮助信息：

`pacman -Th`
