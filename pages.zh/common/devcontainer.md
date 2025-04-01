# devcontainer

> 使用 Docker 容器作为开发环境。
> 更多信息：<https://containers.dev/>.

- 创建并运行一个 Dev Container:

`devcontainer up`

- 将一个 Dev Container 模板应用到工作区:

`devcontainer templates apply --template-id {{template_id}} --template-args {{template_args}} --workspace-folder {{path/to/workspace}}`

- 在当前工作区的运行中的 Dev Container 中执行命令:

`devcontainer exec {{command}}`

- 从 `devcontainer.json` 构建一个 Dev Container 镜像:

`devcontainer build {{path/to/workspace}}`

- 在 VS Code 中打开一个 Dev Container（路径是可选的）:

`devcontainer open {{path/to/workspace}}`

- 从 `devcontainer.json` 读取并打印 Dev Container 的配置:

`devcontainer read-configuration`
