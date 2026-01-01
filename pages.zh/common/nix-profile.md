# nix profile

> 从 Nix 配置集中安装、更新和删除软件包。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-profile.html>.

- 从 nixpkgs 向默认配置集中安装软件包：

`nix profile install {{nixpkgs#软件包1 nixpkgs#软件包2 ...}}`

- 将 GitHub 上某个 flake 中的软件包安装到自定义配置集：

`nix profile install {{github:作者/仓库/软件包}} --profile {{目录路径}}`

- 列出默认配置集中当前已安装的软件包：

`nix profile list`

- 通过名称从默认配置集移除从 nixpkgs 安装的软件包：

`nix profile remove {{legacyPackages.x86_64-linux.软件包}}`

- 将默认配置集中的软件包升级到最新可用版本：

`nix profile upgrade`

- 回滚（撤销）默认配置集上的最近一次操作：

`nix profile rollback`
