# hdiutil

> 用于创建和管理磁盘映像的工具。
> 更多信息：<https://keith.github.io/xcode-man-pages/hdiutil.1.html>。

- 挂载映像：

`hdiutil attach {{path/to/image_file}}`

- 卸载映像：

`hdiutil detach /Volumes/{{volume_file}}`

- 列出已挂载的映像：

`hdiutil info`

- 从目录的内容创建 ISO 映像：

`hdiutil makehybrid -o {{path/to/output_file}} {{path/to/directory}}`