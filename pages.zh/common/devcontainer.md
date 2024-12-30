# 开发容器

> 使用 Docker 容器作为开发环境。
> 更多信息：<https://containers.dev/>.

- 创建并运行一个开发容器：

`devcontainer up`

- 将开发容器模板应用于工作区：

`devcontainer templates apply --template-id {{template_id}} --template-args {{template_args}} --workspace-folder {{path/to/workspace}}`

- 在当前工作区的运行中的开发容器上执行命令：

`devcontainer exec {{command}}`

- 从 `devcontainer.json` 构建开发容器镜像：

`devcontainer build {{path/to/workspace}}`

- 在 VS Code 中打开开发容器（路径是可选的）：

`devcontainer open {{path/to/workspace}}`

- 从 `devcontainer.json` 读取并打印开发容器的配置：

`devcontainer read-configuration`