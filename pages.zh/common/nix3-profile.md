# nix 配置

> 从 Nix 配置中安装、更新和移除软件包。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-profile.html>。

- 从 nixpkgs 安装一些软件包到默认配置中：

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 ...}}`

- 从 GitHub 上的 flake 安装一个软件包到自定义配置中：

`nix profile install {{github:owner/repo/pkg}} --profile {{./path/to/directory}}`

- 列出当前在默认配置中安装的软件包：

`nix profile list`

- 根据名称从默认配置中移除一个从 nixpkgs 安装的软件包：

`nix profile remove {{legacyPackages.x86_64-linux.pkg}}`

- 将默认配置中的软件包升级到最新版本：

`nix profile upgrade`

- 回滚（取消）在默认配置中的最新操作：

`nix profile rollback`