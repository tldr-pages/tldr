# crane digest

> 获取镜像的摘要。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- 获取镜像的摘要：

`crane digest {{image_name}}`

- 打印镜像的完整引用，包括摘要：

`crane digest {{image_name}} --full-ref`

- 指定包含镜像的 tarball 路径：

`crane digest {{image_name}} --tarball {{path/to/tarball}}`

- 显示帮助：

`crane digest {{[-h|--help]}}`
