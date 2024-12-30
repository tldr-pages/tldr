# sbuild

> 在干净的 `chroot` 环境中构建 Debian 二进制包。
> 更多信息：<https://wiki.debian.org/sbuild>。

- 在当前目录中构建包：

`sbuild`

- 构建指定的包：

`sbuild {{package}}`

- 为特定发行版构建：

`sbuild --dist {{distribution}}`

- 使用自定义依赖项进行构建（如果传入一个目录，则使用所有以 `.deb` 结尾的文件）：

`sbuild --extra-package {{path/to/file_or_directory}}`

- 在构建失败时运行一个 shell 以进一步调查：

`sbuild --build-failed-commands=%SBUILD_SHELL`

- 为特定架构进行交叉构建：

`sbuild --host {{architecture}}`

- 为给定的本地架构构建：

`sbuild --arch {{architecture}}`