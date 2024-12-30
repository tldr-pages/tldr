# nix classic

> 一种经典、稳定的接口，针对强大的包管理器，使包管理变得可靠、可重现和声明式。
> 一些 Nix 命令如 `nix-build`、`nix-shell`、`nix-env` 和 `nix-store` 有各自的页面。另请参见: `tldr nix`。
> 更多信息：<https://nixos.org>。

- 通过名称在 nixpkgs 中搜索包：

`nix-env -qaP {{search_term_regexp}}`

- 启动一个可用指定包的 shell：

`nix-shell -p {{pkg1 pkg2 pkg3...}}`

- 永久安装一些包：

`nix-env -iA {{nixpkgs.pkg1 nixpkgs.pkg2...}}`

- 以树形格式显示存储路径（包）的所有依赖项：

`nix-store --query --tree {{/nix/store/...}}`

- 更新通道（仓库）：

`nix-channel --update`

- 从 Nix 存储中删除未使用的路径：

`nix-collect-garbage`