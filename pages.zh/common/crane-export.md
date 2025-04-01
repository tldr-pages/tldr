# crane export

> 将容器镜像的文件系统导出为 tarball。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- 将 tarball 写入 `stdout`:

`crane export {{image_name}} -`

- 将 tarball 写入文件:

`crane export {{image_name}} {{path/to/tarball}}`

- 从 `stdin` 读取镜像:

`crane export - {{path/to/filename}}`