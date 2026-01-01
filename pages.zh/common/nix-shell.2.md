# nix-shell

> 基于一个 Nix 表达式启动交互式 shell。
> 另请参阅：`nix shell.3`。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/nix-shell.html>.

- 使用当前目录下的 `shell.nix` 或 `default.nix` 文件中的 Nix 表达式启动 shell：

`nix-shell`

- 在非交互式 shell 中运行命令并退出：

`nix-shell --run "{{命令}} {{参数1 参数2 ...}}"`

- 使用当前目录中的 `default.nix` 文件中的表达式启动：

`nix-shell {{default.nix}}`

- 从 nixpkgs 加载包后启动 shell：

`nix-shell {{[-p|--packages]}} {{包1 包2 ...}}`

- 通过指定的 nixpkgs 版本加载包后启动 shell：

`nix-shell {{[-p|--packages]}} {{包1 包2 ...}} {{[-I|--include]}} nixpkgs={{https://github.com/NixOS/nixpkgs/archive/nixpkgs版本号.tar.gz}}`

- 在特定的解释器中执行脚本文件的其余部分，（适用于 `#!-scripts`，详见 <https://nixos.org/manual/nix/stable/#use-as-a-interpreter>）：

`nix-shell -i {{解释器}} {{[-p|--packages]}} {{包1 包2 ...}}`

