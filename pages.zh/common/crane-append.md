# crane append

> 基于（可选的）基础镜像推送镜像。
> 附加包含提供的 tarball 内容的层。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>.

- 基于基础镜像推送镜像：

`crane append {{[-b|--base]}} {{image_name}}`

- 附加来自 tarball 的层推送镜像：

`crane append {{[-f|--new_layer]}} {{layer_name1 layer_name2 ...}}`

- 附加带有新标签的层推送镜像：

`crane append {{[-t|--new_tag]}} {{tag_name}}`

- 将生成的镜像推送到新的 tarball：

`crane append {{[-o|--output]}} {{path/to/tarball}}`

- 使用 OCI 媒体类型的空基础镜像，而不是 Docker：

`crane append --oci-empty-base`

- 标注生成的镜像为其基于基础镜像：

`crane append --set-base-image-annotations`

- 显示帮助：

`crane append {{[-h|--help]}}`
