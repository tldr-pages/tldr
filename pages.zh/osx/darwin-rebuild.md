# darwin-rebuild

> 重建并切换到基于 Nix 的 Darwin (macOS) 系统配置。
> 更多信息：<https://github.com/LnL7/nix-darwin>.

- 重建并切换到指定的 Darwin 配置：

`darwin-rebuild switch --flake {{path/to/flake}}`

- 构建配置但不切换到它：

`darwin-rebuild build --flake {{path/to/flake}}`

- 显示帮助：

`darwin-rebuild --help`