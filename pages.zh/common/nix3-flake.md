# nix flake

> 管理 Nix flakes。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-flake.html>。

- 从默认模板在当前目录创建一个新的 flake（仅 `flake.nix` 文件）：

`nix flake init`

- 更新当前目录中 flake 的所有输入（依赖项）：

`nix flake update`

- 更新当前目录中 flake 的特定输入（依赖项）：

`nix flake lock --update-input {{input}}`

- 显示 GitHub 上 flake 的所有输出：

`nix flake show {{github:owner/repo}}`

- 显示帮助：

`nix flake --help`