# crane digest

> 获取图像的摘要。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>。

- 获取图像的摘要：

`crane digest {{image_name}}`

- 按摘要打印完整图像引用：

`crane digest {{image_name}} --full-ref`

- 指定包含图像的tar包路径：

`crane digest {{image_name}} --tarball {{path/to/tarball}}`

- 显示帮助信息：

`crane digest {{-h|--help}}`