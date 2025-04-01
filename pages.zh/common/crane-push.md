# crane push

> 将本地镜像内容推送到远程仓库。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>.

- 将本地镜像推送到远程仓库：

`crane push {{path/to/tarball}} {{image_name}}`

- 包含已发布镜像引用列表的文件路径：

`crane push {{path/to/tarball}} {{image_name}} --image-refs {{path/to/filename}}`

- 作为一个索引推送多个镜像（如果路径包含多个镜像时必需）：

`crane push {{path/to/tarball}} {{image_name}} --index`

- 显示帮助信息：

`crane push {{[-h|--help]}}`