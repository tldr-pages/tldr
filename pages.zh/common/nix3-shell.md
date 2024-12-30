# nix shell

> 启动一个可以使用指定软件包的 shell。
> 另请参见：`nix-shell` 用于设置开发环境，`nix3 flake` 获取有关 flake 的信息。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-shell.html>。

- 启动一个交互式 Shell，包含来自 `nixpkgs` 的一些软件包：

`nix shell {{nixpkgs#pkg1 nixpkgs#packageSet.pkg2 ...}}`

- 启动一个提供来自旧版本 `nixpkgs`（21.05）的软件包的 Shell：

`nix shell {{nixpkgs/nixos-21.05#pkg}}`

- 启动一个带有当前目录中 flake 的“默认软件包”的 Shell，如果有构建发生，打印构建日志：

`nix shell -L`

- 启动一个带有来自 GitHub 上 flake 的软件包的 Shell：

`nix shell {{github:owner/repo#pkg}}`

- 在一个带有软件包的 Shell 中运行命令：

`nix shell {{nixpkgs#pkg}} -c {{some-cmd --someflag '其他参数'}}`