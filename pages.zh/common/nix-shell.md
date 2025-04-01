# nix-shell

> 根据 Nix 表达式启动一个交互式 shell。
> 另见：`nix3 shell`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/nix-shell.html>。

- 使用当前目录中的 `shell.nix` 或 `default.nix` 启动 nix 表达式：

`nix-shell`

- 在非交互式 shell 中运行 shell 命令并退出：

`nix-shell --run "{{command}} {{argument1 argument2 ...}}"`

- 使用当前目录中的 `default.nix` 启动：

`nix-shell {{default.nix}}`

- 使用从 nixpkgs 加载的包启动：

`nix-shell --packages {{package1 package2 ...}}`

- 使用从特定 nixpkgs 修订版加载的包启动：

`nix-shell --packages {{package1 package2 ...}} -I nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs_revision.tar.gz}}`

- 在特定解释器中评估文件的其余部分，用于 `#!-scripts`（参见：<https://nixos.org/manual/nix/stable/#use-as-a-interpreter>）：

`nix-shell -i {{interpreter}} --packages {{package1 package2 ...}}`
