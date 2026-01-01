# nix search

> 在 Nix Flake 中搜索软件包。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-search.html>.

- 在 `nixpkgs` 中根据软件包名称或描述进行搜索：

`nix search {{nixpkgs}} {{搜索关键词}}`

- 显示 nixpkgs 中某个软件包的详细描述：

`nix search {{nixpkgs#软件包名}}`

- 查看 GitHub 上某 Flake 仓库提供的所有可用软件包：

`nix search {{github:所有者/仓库名}}`
