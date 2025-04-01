# nix-env

> 操作或查询 Nix 用户环境。
> 更多信息：<https://nixos.org/manual/nix/stable/#sec-nix-env>.

- 列出所有已安装的软件包：

`nix-env -q`

- 查询已安装的软件包：

`nix-env -q {{search_term}}`

- 查询可用的软件包：

`nix-env -qa {{search_term}}`

- 安装软件包：

`nix-env -iA nixpkgs.{{pkg_name}}`

- 从 URL 安装软件包：

`nix-env -i {{pkg_name}} --file {{example.com}}`

- 卸载软件包：

`nix-env -e {{pkg_name}}`

- 升级一个软件包：

`nix-env -u {{pkg_name}}`

- 升级所有软件包：

`nix-env -u`
