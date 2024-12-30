# nix-build

> 构建一个 Nix 表达式。
> 另见：`nix3 build`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/nix-build.html>。

- 构建一个 Nix 表达式：

`nix-build '<nixpkgs>' --attr {{firefox}}`

- 构建一个沙箱化的 Nix 表达式（在非 NixOS 上）：

`nix-build '<nixpkgs>' --attr {{firefox}} --option sandbox true`