# crane pull

> 通过引用拉取远程镜像并将其内容存储在本地。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>。

- 拉取远程镜像：

`crane pull {{image_name}} {{path/to/tarball}}`

- 在使用 --format=oci 时，将用于拉取的镜像引用保留为注释：

`crane pull {{image_name}} {{path/to/tarball}} --annotate-ref`

- 缓存镜像层的路径：

`crane pull {{image_name}} {{path/to/tarball}} {{-c|--cache_path}} {{path/to/cache}}`

- 保存镜像的格式（默认 'tarball'）：

`crane pull {{image_name}} {{path/to/tarball}} {{-format}} {{format_name}}`

- 显示帮助：

`crane pull {{-h|--help}}`