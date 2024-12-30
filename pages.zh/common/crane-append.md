# crane append

> 基于（可选）基础镜像推送一个镜像。
> 附加包含所提供 tarball 内容的层。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>。

- 基于基础镜像推送镜像：

`crane append {{-b|--base}} {{image_name}}`

- 从 tarball 推送附加层的镜像：

`crane append {{-f|--new_layer}} {{layer_name1 layer_name2 ...}}`

- 推送带有新标签的附加层的镜像：

`crane append {{-t|--new_tag}} {{tag_name}}`

- 将生成的镜像推送到新的 tarball：

`crane append {{-o|--output}} {{path/to/tarball}}`

- 使用类型为 OCI 媒体的空基础镜像，而不是 Docker：

`crane append --oci-empty-base`

- 将生成的镜像注解为基于基础镜像：

`crane append --set-base-image-annotations`

- 显示帮助信息：

`crane append {{-h|--help}}`