# pacman --upgrade

> Arch Linux 包管理器工具。
> 另见：`pacman`。
> 更多信息：<https://manned.org/pacman.8>。

- 从文件中安装一个或多个软件包：

`sudo pacman -U {{path/to/package1.pkg.tar.zst}} {{path/to/package2.pkg.tar.zst}}`

- 安装软件包时不提示：

`sudo pacman -U --noconfirm {{path/to/package.pkg.tar.zst}}`

- 在软件包安装期间覆盖冲突文件：

`sudo pacman -U --overwrite {{path/to/file}} {{path/to/package.pkg.tar.zst}}`

- 安装软件包，跳过依赖 [(d)] 版本检查：

`sudo pacman -Ud {{path/to/package.pkg.tar.zst}}`

- 获取并 [p]rint 将受到升级影响的软件包（不安装任何软件包）：

`pacman -Up {{path/to/package.pkg.tar.zst}}`

- 显示帮助：

`pacman -U --help`