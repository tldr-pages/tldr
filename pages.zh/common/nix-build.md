# nix-build

> 构建一个 Nix 表达式。
> 请参阅：`nix3 build`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/nix-build.html>。

- 构建一个 Nix 表达式：

`nix-build '<nixpkgs>' --attr {{firefox}}`

- 构建一个沙盒化的 Nix 表达式（仅限非 NixOS 系统）：

`nix-build '<nixpkgs>' --attr {{firefox}} --option sandbox true`
