# nix profile

> 在 Nix 配置文件中安装、更新和删除包。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-profile.html>.

- 从 nixpkgs 安装一些包到默认配置文件中：

`nix profile install {{nixpkgs#pkg1 nixpkgs#pkg2 ...}}`

- 从 GitHub 上的一个 flake 安装包到自定义配置文件中：

`nix profile install {{github:owner/repo/pkg}} --profile {{./path/to/directory}}`

- 列出默认配置文件中当前已安装的包：

`nix profile list`

- 从默认配置文件中按名称删除一个从 nixpkgs 安装的包：

`nix profile remove {{legacyPackages.x86_64-linux.pkg}}`

- 将默认配置文件中的包升级到最新可用版本：

`nix profile upgrade`

- 撤销默认配置文件上的最新操作：

`nix profile rollback`