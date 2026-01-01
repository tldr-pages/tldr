# nix develop

> 运行一个提供派生构建环境的 Bash 终端。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-develop.html>.

- 启动一个包含 nixpkgs 中某个程序包所有依赖项的终端：

`nix develop {{nixpkgs#程序包名}}`

- 在当前目录的 flake 中启动默认程序包的开发终端：

`nix develop`

- 在该终端中配置并构建源代码：

`configurePhase; buildPhase`
