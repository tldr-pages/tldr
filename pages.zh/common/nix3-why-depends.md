# nix why-depends

> 显示一个包为何依赖于另一个包。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>.

- 显示当前运行的 NixOS 系统为何需要某个存储路径：

`nix why-depends {{/run/current-system}} {{/nix/store/...}}`

- 显示 nixpkgs 中的一个包为何需要另一个包作为 _构建时_ 依赖：

`nix why-depends --derivation {{nixpkgs#dependent}} {{nixpkgs#dependency}}`