# nix

> 一款强大的包管理器，使包管理变得可靠、可重现和声明式。
> `nix` 是实验性的，需要启用实验功能。有关经典、稳定的接口，请参见 `tldr nix classic`。
> 一些子命令，如 `build`、`develop`、`flake`、`registry`、`profile`、`search`、`repl`、`store`、`edit`、`why-depends` 等，有其自己的使用文档。
> 更多信息：<https://nixos.org/manual/nix>。

- 启用 `nix` 命令：

`mkdir -p ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- 通过名称或描述在 nixpkgs 中搜索包：

`nix search nixpkgs {{search_term}}`

- 启动一个包含指定 nixpkgs 包的 shell：

`nix shell {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- 永久安装一些来自 nixpkgs 的包：

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- 从 Nix 存储中删除未使用的路径以释放空间：

`nix store gc`

- 启动一个用于评估 Nix 表达式的交互环境：

`nix repl`

- 显示特定子命令的帮助：

`nix help {{subcommand}}`