# debtap

> 将 Debian 包转换为 Arch Linux 包。
> 参见：`pacman-upgrade`。
> 更多信息：<https://github.com/helixarch/debtap>。

- 更新 debtap 数据库（首次运行前）：

`sudo debtap --update`

- 转换指定的包：

`debtap {{path/to/package.deb}}`

- 转换指定的包，跳过所有问题，除了编辑元数据文件：

`debtap --quiet {{path/to/package.deb}}`

- 生成 PKGBUILD 文件：

`debtap --pkgbuild {{path/to/package.deb}}`
