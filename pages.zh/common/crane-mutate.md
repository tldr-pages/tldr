# crane mutate

> 修改镜像的标签和注解。
> 容器必须推送到注册表，并在注册表中更新其清单。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>.

- 要设置的新注解（默认 []）：

`crane mutate {{[-a|--annotation]}}/{{[-l|--label]}} {{annotation/label}}`

- 要添加到镜像的 tarball、命令、入口点、环境变量或暴露的端口路径：

`crane mutate {{--append}}/{{--cmd}}/{{--entrypoint}}/{{[-e|--env]}}/{{--exposed-ports}} {{var1 var2 ...}}`

- 结果镜像的新 tarball 路径：

`crane mutate {{[-o|--output]}} {{path/to/tarball}}`

- 要推送到的仓库，形式为 os/arch{{/variant}}{{:osversion}}{{,<platform>}}：

`crane mutate --set-platform {{platform_name}}`

- 要应用于修改后的镜像的新标签引用：

`crane mutate {{[-t|--tag]}} {{tag_name}}`

- 要设置的新用户：

`crane mutate {{[-u|--user]}} {{username}}`

- 要设置的新工作目录：

`crane mutate {{[-w|--workdir]}} {{path/to/workdir}}`

- 显示帮助：

`crane mutate {{[-h|--help]}}`
