# nix classic

> 提供了一个稳定且传统的接口，用于一个强大的软件包管理器，使得软件包管理变得可靠、可重复且声明式。
> 一些 Nix 命令，如 `nix-build`、`nix-shell`、`nix-env` 和 `nix-store` 有独立的页面。另见：`tldr nix`。
> 更多信息：<https://nixos.org>。

- 通过名称在 nixpkgs 中搜索软件包：

`nix-env -qaP {{search_term_regexp}}`

- 启动一个包含指定软件包的 Shell：

`nix-shell -p {{pkg1 pkg2 pkg3...}}`

- 永久安装一些软件包：

`nix-env -iA {{nixpkgs.pkg1 nixpkgs.pkg2...}}`

- 以树状格式显示存储路径（软件包）的所有依赖项：

`nix-store --query --tree {{/nix/store/...}}`

- 更新通道（仓库）：

`nix-channel --update`

- 从 Nix 存储中删除未使用的路径：

`nix-collect-garbage`