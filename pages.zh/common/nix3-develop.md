# nix develop

> 运行一个提供派生包构建环境的 Bash shell。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html>。

- 启动一个包含 nixpkgs 中包所有依赖项的 shell：

`nix develop {{nixpkgs#pkg}}`

- 启动当前目录中flake的默认包的开发shell：

`nix develop`

- 在该 shell 中，配置和构建源代码：

`configurePhase; buildPhase`
