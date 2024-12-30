# nix why-depends

> 显示一个软件包为什么依赖于另一个软件包。
> 更多信息请访问：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>。

- 显示当前运行的 NixOS 系统为什么需要某个存储路径：

`nix why-depends {{/run/current-system}} {{/nix/store/...}}`

- 显示来自 nixpkgs 的一个软件包为什么将另一个软件包作为 _构建时_ 依赖：

`nix why-depends --derivation {{nixpkgs#dependent}} {{nixpkgs#dependency}}`