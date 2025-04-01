# flatpak-builder

> 帮助构建应用程序依赖项。
> 更多信息：<https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>.

- 构建 Flatpak 并将其导出到新仓库：

`flatpak-builder {{path/to/build_directory}} {{path/to/manifest}}`

- 构建 Flatpak 并将其导出到指定仓库：

`flatpak-builder --repo={{repository_name}} {{path/to/build_directory}} {{path/to/manifest}}`

- 构建 Flatpak 并本地安装：

`flatpak-builder --install {{path/to/build_directory}} {{path/to/manifest}}`

- 构建并签名 Flatpak，然后将其导出到指定仓库：

`flatpak-builder --gpg-sign={{key_id}} --repo={{repository_name}} {{path/to/manifest}}`

- 在应用程序沙箱内运行 shell 而不进行安装：

`flatpak-builder --run {{path/to/build_directory}} {{path/to/manifest}} {{sh}}`
