# toolbox run

> 在现有的 `toolbox` 容器中运行命令。
> 参见：`toolbox enter`。
> 更多信息：<https://manned.org/toolbox-run>。

- 在特定的 `toolbox` 容器中运行命令：

`toolbox run --container {{container_name}} {{command}}`

- 在特定版本的发行版的 `toolbox` 容器中运行命令：

`toolbox run --distro {{distribution}} --release {{release}} {{command}}`

- 使用 Fedora 39 的默认镜像在 `toolbox` 容器中运行 `emacs`：

`toolbox run --distro {{fedora}} --release {{f39}} {{emacs}}`