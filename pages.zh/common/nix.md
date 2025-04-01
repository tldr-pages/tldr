# nix

> 一个强大的包管理器，使包管理可靠、可重现且声明式。
> `nix` 是实验性的，需要启用实验性功能。对于传统且稳定的接口，请参见 `tldr nix classic`。
> 一些子命令如 `build`、`develop`、`flake`、`registry`、`profile`、`search`、`repl`、`store`、`edit`、`why-depends` 等都有自己的使用文档。
> 更多信息：<https://nixos.org/manual/nix>.

- 启用 `nix` 命令:

`mkdir -p ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- 通过名称或描述在 nixpkgs 中搜索包:

`nix search nixpkgs {{search_term}}`

- 启动一个包含从 nixpkgs 指定的包的 shell:

`nix shell {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- 从 nixpkgs 永久安装一些包:

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- 从 Nix 存储中删除未使用的路径以释放空间:

`nix store gc`

- 启动一个用于评估 Nix 表达式的交互式环境:

`nix repl`

- 显示特定子命令的帮助:

`nix help {{subcommand}}`