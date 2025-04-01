# home-manager

> 使用 Nix 管理每个用户的环境，允许声明式配置用户的主目录。
> 更多信息：<https://github.com/nix-community/home-manager>.

- 构建 `~/.config/nixpkgs/home.nix` 中定义的配置，但不应用它：

`home-manager build`

- 构建并应用（切换到）新配置：

`home-manager switch`

- 回滚到以前的配置版本：

`home-manager rollback`

- 列出所有现有的配置版本：

`home-manager generations`

- 使用 flakes 时，通过传递 flake 的路径来运行需要 nix 执行的任何操作（构建、切换、新闻）：

`home-manager {{command}} --flake {{path/to/flake}}`