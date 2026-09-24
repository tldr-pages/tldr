# docker image save

> 将 Docker 镜像导出到归档文件。
> 更多信息：<https://docs.docker.com/reference/cli/docker/image/save/>。

- 通过将 `stdout` 重定向到 `.tar` 归档文件来保存镜像：

`docker {{[save|image save]}} {{镜像}}:{{标签}} > {{路径/到/文件.tar}}`

- 将镜像保存到 `.tar` 归档文件：

`docker {{[save|image save]}} {{[-o|--output]}} {{路径/到/文件.tar}} {{镜像}}:{{标签}}`

- 保存镜像的所有标签：

`docker {{[save|image save]}} {{[-o|--output]}} {{路径/到/文件.tar}} {{镜像名称}}`

- 选择镜像的特定标签进行保存：

`docker {{[save|image save]}} {{[-o|--output]}} {{路径/到/文件.tar}} {{镜像名称:标签1 镜像名称:标签2 ...}}`
