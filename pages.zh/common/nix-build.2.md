# nix-build

> 构建 Nix 表达式。
> 另请参阅：`nix build.3`。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/nix-build.html>。

- 构建 Nix 表达式：

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{包名}}`

- 构建沙盒化的 Nix 表达式（在非 NixOS 系统上）：

`nix-build '<nixpkgs>' {{[-A|--attr]}} {{包名}} --option sandbox true`

