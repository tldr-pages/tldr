# nix flake

> 管理 Nix Flakes。
> 此命令也有关于其子命令的文件，例如：`init`、`show`、`info`.
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-flake.html>。

- 更新当前目录下 Flake 的所有输入（依赖项）：

`nix flake update`

- 仅更新当前目录下 Flake 的指定输入（依赖项）：

`nix flake update {{输入项}}`

- 克隆包含 Flake 的 GitHub 仓库：

`nix flake clone {{github:所有者/仓库名#属性}}`

- 为指定目录中的 Flake 创建缺失的锁文件记录：

`nix flake lock {{flake路径}}`

- 显示帮助：

`nix flake --help`
