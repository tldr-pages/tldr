# crane flatten

> 将镜像的所有层合并为单层。
> 如果未指定标签，则将摘要推送到原始镜像仓库。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>。

- 合并镜像的层：

`crane flatten`

- 为合并后的镜像应用新标签：

`crane flatten {{[-t|--tag]}} {{tag_name}}`

- 显示帮助信息：

`crane flatten {{[-h|--help]}}`
