# nixos-container

> 使用 Linux 容器启动 NixOS 容器。
> 更多信息：<https://nixos.org/manual/nixos/stable/#ch-containers>。

- 列出正在运行的容器：

`sudo nixos-container list`

- 使用特定配置文件创建一个 NixOS 容器：

`sudo nixos-container create {{container_name}} --config-file {{nix_config_file_path}}`

- 启动、停止、终止或销毁一个特定的容器：

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{container_name}}`

- 在一个正在运行的容器中运行一个命令：

`sudo nixos-container run {{container_name}} -- {{command}} {{command_arguments}}`

- 更新一个容器的配置：

`sudo $EDITOR /var/lib/container/{{container_name}}/etc/nixos/configuration.nix && sudo nixos-container update {{container_name}}`

- 进入一个已经运行的容器的交互式 shell 会话：

`sudo nixos-container root-login {{container_name}}`
