# crane 扁平化

> 将图像的层扁平化为单个层。
> 如果未指定标签，则将摘要推送到原始图像库。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>。

- 扁平化图像：

`crane flatten`

- 对扁平化后的图像应用新标签：

`crane flatten {{-t|--tag}} {{tag_name}}`

- 显示帮助：

`crane flatten {{-h|--help}}`