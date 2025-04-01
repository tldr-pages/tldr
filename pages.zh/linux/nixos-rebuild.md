# nixos-rebuild

> 重新配置 NixOS 机器。
> 更多信息：<https://nixos.org/nixos/manual/#sec-changing-config>。

- 构建并切换到新配置，使其成为默认启动配置：

`sudo nixos-rebuild switch`

- 构建并切换到新配置，使其成为默认启动配置并命名启动项：

`sudo nixos-rebuild switch -p {{name}}`

- 构建并切换到新配置，使其成为默认启动配置并安装更新：

`sudo nixos-rebuild switch --upgrade`

- 回滚配置更改，切换到上一个版本：

`sudo nixos-rebuild switch --rollback`

- 构建新配置并设为默认启动配置，但不切换到新配置：

`sudo nixos-rebuild boot`

- 构建并激活新配置，但不创建启动项（用于测试）：

`sudo nixos-rebuild test`

- 构建配置并在虚拟机中打开：

`sudo nixos-rebuild build-vm`
