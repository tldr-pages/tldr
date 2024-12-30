# nix 开发

> 运行一个提供派生构建环境的 Bash shell。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>。

- 启动一个 shell，其中包含来自 nixpkgs 的软件包的所有依赖项：

`nix develop {{nixpkgs#pkg}}`

- 为当前目录中的 flake 默认软件包启动一个开发 shell：

`nix develop`

- 在该 shell 中，配置并构建源代码：

`configurePhase; buildPhase`