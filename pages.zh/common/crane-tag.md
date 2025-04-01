# crane tag

> 无需下载即可高效地标记远程镜像，与 `copy` 命令不同。
> 由于我们知道清单已经存在，因此它会跳过层存在性检查，从而稍微快一些。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

- 标记远程镜像：

`crane tag {{image_name}} {{tag_name}}`

- 显示帮助：

`crane tag {{[-h|--help]}}`