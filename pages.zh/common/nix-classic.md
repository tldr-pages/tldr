# nix classic

> Nix 包管理器经典、稳定的接口，使得包管理变得可靠、可复现且可声明。
> 部分 Nix 命令，例如 `nix-build`、`nix-shell`、`nix-env` 和 `nix-store`，拥有各自的页面。
> 另请参阅：`nix`。
> 更多信息：<https://nixos.org/>。

- 通过包名在 nixpkgs 中搜索包：

`nix-env {{[-qaP|--query --available --attr-path]}} {{搜索词正则表达式}}`

- 启动一个包含指定可用的 shell：

`nix-shell {{[-p|--packages]}} {{包1 包2 包3 ...}}`

- 永久安装某些包：

`nix-env {{[-iA|--install --attr]}} {{nixpkgs.包1 nixpkgs.包2 ...}}`

- 以树状格式展示存储路径（包）的所有依赖：

`nix-store {{[-q|--query]}} --tree /nix/store/{{校验和-包名-版本.扩展名}}`

- 更新频道（仓库源）：

`nix-channel --update`

- 从 Nix 存储中移除未使用的路径：

`nix-collect-garbage`
