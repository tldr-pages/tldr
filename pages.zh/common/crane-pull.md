# crane pull

> 通过引用拉取远程镜像，并将它们的内容存储在本地。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>.

- 拉取远程镜像：

`crane pull {{image_name}} {{path/to/tarball}}`

- 使用 --format=oci 时，保留用于拉取镜像的引用作为注释：

`crane pull {{image_name}} {{path/to/tarball}} --annotate-ref`

- 用于缓存镜像层的路径：

`crane pull {{image_name}} {{path/to/tarball}} {{[-c|--cache_path]}} {{path/to/cache}}`

- 保存镜像的格式（默认为 'tarball'）：

`crane pull {{image_name}} {{path/to/tarball}} {{-format}} {{format_name}}`

- 显示帮助：

`crane pull {{[-h|--help]}}`
