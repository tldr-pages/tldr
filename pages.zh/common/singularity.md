# 奇点

> 管理奇点容器和镜像。
> 更多信息：<https://singularity-docs.readthedocs.io/en/latest/#commands>。

- 从 Sylabs Cloud 下载远程镜像：

`singularity pull --name {{image.sif}} {{library://godlovedc/funny/lolcow:latest}}`

- 使用最新的奇点镜像格式重建远程镜像：

`singularity build {{image.sif}} {{docker://godlovedc/lolcow}}`

- 从镜像启动一个容器并进入其内部的 shell：

`singularity shell {{image.sif}}`

- 从镜像启动一个容器并运行一个命令：

`singularity exec {{image.sif}} {{command}}`

- 从镜像启动一个容器并执行内部的运行脚本：

`singularity run {{image.sif}}`

- 从配方文件构建一个奇点镜像：

`sudo singularity build {{image.sif}} {{recipe}}`