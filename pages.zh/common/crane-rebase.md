# crane rebase

> 将一个镜像重新基于一个新的基础镜像。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- 重新基于镜像：

`crane rebase`

- 要插入的新基础镜像：

`crane rebase --new_base {{image_name}}`

- 要移除的旧基础镜像：

`crane rebase --old_base {{image_name}}`

- 要应用于重新基于的镜像的标签：

`crane rebase {{[-t|--tag]}} {{tag_name}}`

- 显示帮助：

`crane rebase {{[-h|--help]}}`