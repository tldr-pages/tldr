# nix

> 一款强大的包管理器，让包管理变得可靠、可重现且可声明。
> `nix` 是实验性功能，需启用实验特性。
> 部分子命令如 `build`、`develop`、`flake`、`registry`、`profile`、`search`、`repl`、`store`、`edit`、`why-depends` 等均有其独立的用法说明。
> 另请参阅：`nix classic`。
> 更多信息： <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix>。

- 启用 `nix` 命令：

`mkdir {{[-p|--parents]}} ~/.config/nix; echo 'experimental-features = nix-command flakes' > ~/.config/nix/nix.conf`

- 根据名称或描述在 nixpkgs 中搜索软件包：

`nix search nixpkgs {{search_term}}`

- 启动一个 shell，使其可以访问 nixpkgs 中指定的软件包：

`nix shell {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- 从 nixpkgs 中永久安装某些软件包：

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 nixpkgs#pkg3 ...}}`

- 从 Nix 存储中移除未使用的路径以释放空间：

`nix store gc`

- 启动一个用于评估 Nix 表达式的交互式环境：

`nix repl`

- 显示特定子命令的帮助信息：

`nix help {{subcommand}}`
