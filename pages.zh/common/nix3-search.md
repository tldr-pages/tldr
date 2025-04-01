# nix search

> 在 Nix flake 中搜索软件包。
> 参见：`nix3 flake` 了解有关 flake 的信息。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-search.html>。

- 根据名称或描述在 `nixpkgs` 中搜索软件包：

`nix search {{nixpkgs}} {{search_term...}}`

- 显示来自 nixpkgs 的软件包的描述：

`nix search {{nixpkgs#pkg}}`

- 显示来自 github 上 flake 的所有可用软件包：

`nix search {{github:owner/repo}}`