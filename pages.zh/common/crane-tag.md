# crane 标签

> 高效地标记远程镜像而无需下载，这与 `copy` 命令不同。
> 它跳过了层存在性检查，因为我们知道清单已经存在，这使得它稍微更快。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>。

- 标记远程镜像：

`crane tag {{image_name}} {{tag_name}}`

- 显示帮助信息：

`crane tag {{-h|--help}}`