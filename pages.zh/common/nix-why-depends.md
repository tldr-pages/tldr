# nix why-depends

> 用于查询某个包为何依赖于另一个包。
> 更多信息： <https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-why-depends.html>。

- 显示当前运行的 NixOS 系统为何需要某个存储路径：

`nix why-depends {{/run/current-system}} /nix/store/{{checksum-package-version.ext}}`

- 显示 nixpkgs 中的某个包为何将另一个包作为**构建时**依赖：

`nix why-depends --derivation {{nixpkgs#dependent}} {{nixpkgs#dependency}}`
