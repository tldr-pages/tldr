# nix shell

> 启动一个指定包可用的 shell。
> 参见：`nix-shell` 用于设置开发环境，`nix3 flake` 了解有关 flakes 的信息。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-shell.html>.

- 使用 `nixpkgs` 中的一些包启动一个交互式 shell：

`nix shell {{nixpkgs#pkg1 nixpkgs#packageSet.pkg2 ...}}`

- 使用 `nixpkgs` 的旧版本（21.05）中的包启动一个 shell：

`nix shell {{nixpkgs/nixos-21.05#pkg}}`

- 使用当前目录下的 flake 的“默认包”启动一个 shell，如果有构建则打印构建日志：

`nix shell -L`

- 使用 GitHub 上的 flake 中的包启动一个 shell：

`nix shell {{github:owner/repo#pkg}}`

- 在包含指定包的 shell 中运行一个命令：

`nix shell {{nixpkgs#pkg}} -c {{some-cmd --someflag 'Some other arguments'}}`