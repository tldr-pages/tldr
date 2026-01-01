# nix-channel

> 管理 `nix` 更新频道。
> 更多信息请查看：<https://nixos.wiki/wiki/Nix_channels>。

- 列出当前频道：

`nix-channel --list`

- 添加频道：

`nix-channel --add {{https://nixos.org/channels/nixpkgs-unstable}}`

- 更新所有频道的软件包列表：

`nix-channel --update`