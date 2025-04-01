# nixos-option

> 检查 NixOS 配置。
> 更多信息：<https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- 列出给定选项键的所有子键：

`nixos-option {{option_key}}`

- 列出当前启动内核模块：

`nixos-option boot.kernelModules`

- 列出特定用户的授权密钥：

`nixos-option users.users.{{username}}.openssh.authorizedKeys.{{keyFiles|keys}}`

- 列出所有远程构建器：

`nixos-option nix.buildMachines`

- 列出另一个 NixOS 配置中给定键的所有子键：

`NIXOS_CONFIG={{path_to_configuration.nix}} nixos-option {{option_key}}`

- 递归显示用户的所有值：

`nixos-option -r users.users.{{user}}`