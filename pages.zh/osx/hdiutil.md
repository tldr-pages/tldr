# hdiutil

> 用于创建和管理磁盘镜像的工具。
> 更多信息：<https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- 挂载镜像：

`hdiutil attach {{path/to/image_file}}`

- 卸载镜像：

`hdiutil detach /Volumes/{{volume_file}}`

- 列出已挂载的镜像：

`hdiutil info`

- 从目录内容创建 ISO 镜像：

`hdiutil makehybrid -o {{path/to/output_file}} {{path/to/directory}}`
