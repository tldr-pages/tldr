# crane push

> 将本地镜像内容推送到远程注册中心。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>。

- 将本地镜像推送到远程注册中心：

`crane push {{path/to/tarball}} {{image_name}}`

- 包含已发布镜像引用列表的文件路径：

`crane push {{path/to/tarball}} {{image_name}} --image-refs {{path/to/filename}}`

- 将一组镜像作为单个索引推送（如果路径中有多个镜像，则需要）：

`crane push {{path/to/tarball}} {{image_name}} --index`

- 显示帮助信息：

`crane push {{-h|--help}}`