# home-manager

> 使用 Nix 管理每个用户的环境，允许声明性配置用户的主目录。
> 更多信息：<https://github.com/nix-community/home-manager>。

- 构建在 `~/.config/nixpkgs/home.nix` 中定义的配置，但不应用它：

`home-manager build`

- 构建并应用（切换到）新的配置：

`home-manager switch`

- 构建用于测试的配置，但不应用它：

`home-manager test`

- 回滚到之前的配置版本：

`home-manager rollback`

- 列出所有现有的配置版本：

`home-manager generations`