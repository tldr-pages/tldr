# crane 验证

> 验证镜像是否格式正确。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>。

- 验证一个镜像：

`crane validate`

- 跳过下载/摘要层：

`crane validate --fast`

- 要验证的远程镜像名称：

`crane validate --remote {{image_name}}`

- 要验证的 tarball 路径：

`crane validate --tarball {{path/to/tarball}}`

- 显示帮助：

`crane validate {{-h|--help}}`