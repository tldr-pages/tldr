# sbuild

> 在干净的 `chroot` 环境中构建 Debian 二进制包。
> 更多信息：<https://wiki.debian.org/sbuild>.

- 构建当前目录中的包：

`sbuild`

- 构建指定的包：

`sbuild {{package}}`

- 为特定的发行版构建：

`sbuild --dist {{distribution}}`

- 使用自定义依赖项构建（如果传递的是目录，则使用所有以 `.deb` 结尾的文件）：

`sbuild --extra-package {{path/to/file_or_directory}}`

- 构建失败时运行一个 shell 进行进一步调查：

`sbuild --build-failed-commands=%SBUILD_SHELL`

- 为特定架构进行交叉构建：

`sbuild --host {{architecture}}`

- 为指定的本机架构构建：

`sbuild --arch {{architecture}}`