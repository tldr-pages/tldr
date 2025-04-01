# pacman --upgrade

> Arch Linux 包管理工具。
> 参见: `pacman`。
> 更多信息: <https://manned.org/pacman.8>。

- 从文件中安装一个或多个包：

`sudo pacman -U {{path/to/package1.pkg.tar.zst}} {{path/to/package2.pkg.tar.zst}}`

- 不提示直接安装包：

`sudo pacman -U --noconfirm {{path/to/package.pkg.tar.zst}}`

- 在安装包时覆盖冲突的文件：

`sudo pacman -U --overwrite {{path/to/file}} {{path/to/package.pkg.tar.zst}}`

- 安装包时跳过依赖版本检查：

`sudo pacman -Ud {{path/to/package.pkg.tar.zst}}`

- 获取并打印将被升级影响的包（不会实际安装任何包）：

`pacman -Up {{path/to/package.pkg.tar.zst}}`

- 显示帮助：

`pacman -Uh`