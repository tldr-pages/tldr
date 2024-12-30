# flatpak-builder

> 帮助构建应用程序依赖项。
> 更多信息：<https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>。

- 构建一个 Flatpak 并将其导出到一个新的仓库：

`flatpak-builder {{path/to/build_directory}} {{path/to/manifest}}`

- 构建一个 Flatpak 并将其导出到指定的仓库：

`flatpak-builder --repo={{repository_name}} {{path/to/build_directory}} {{path/to/manifest}}`

- 构建一个 Flatpak 并在本地安装：

`flatpak-builder --install {{path/to/build_directory}} {{path/to/manifest}}`

- 构建并签名一个 Flatpak 并将其导出到指定的仓库：

`flatpak-builder --gpg-sign={{key_id}} --repo={{repository_name}} {{path/to/manifest}}`

- 在应用程序沙箱内运行一个 shell 而不安装它：

`flatpak-builder --run {{path/to/build_directory}} {{path/to/manifest}} {{sh}}`