# crane mutate

> 修改图像标签和注释。
> 容器必须推送到注册表，并在那里更新清单。
> 更多信息：<https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>。

- 要设置的新注释（默认 []）：

`crane mutate {{-a|--annotation}}/{{-l|--label}} {{annotation/label}}`

- 要附加到图像的 tarball/命令/入口点/环境变量/暴露端口的路径：

`crane mutate {{--append}}/{{--cmd}}/{{--entrypoint}}/{{-e|--env}}/{{--exposed-ports}} {{var1 var2 ...}}`

- 结果图像的新 tarball 路径：

`crane mutate {{-o|--output}} {{path/to/tarball}}`

- 以 os/arch{{/variant}}{{:osversion}}{{,<platform>}} 形式推送变异图像的存储库：

`crane mutate --set-platform {{platform_name}}`

- 要应用于变异图像的新标签引用：

`crane mutate {{-t|--tag}} {{tag_name}}`

- 要设置的新用户：

`crane mutate {{-u|--user}} {{username}}`

- 要设置的新工作目录：

`crane mutate {{-w|--workdir}} {{path/to/workdir}}`

- 显示帮助信息：

`crane mutate {{-h|--help}}`