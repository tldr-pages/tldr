# nix shell

> 启动一个包含指定软件包的交互式 Shell 环境。
> 另请参阅：`nix-shell`, `nix flake`。
> 更多信息：<https://manned.org/nix3-shell>。

- 从 `nixpkgs` 中选取部分软件包启动交互式 Shell：

`nix shell {{nixpkgs#包1 nixpkgs#软件包组.包2 ...}}`

- 使用旧版 `nixpkgs`（21.05）中的软件包启动 Shell：

`nix shell {{nixpkgs/nixos-21.05#软件包}}`

- 从当前目录的 flake 使用“默认软件包”启动 Shell（若发生构建则显示日志）：

`nix shell -L`

- 使用GitHub上 flake 中的软件包启动 Shell：

`nix shell {{github:所有者/仓库#软件包}}`

- 在含指定软件包的 Shell 环境中运行命令：

`nix shell {{nixpkgs#软件包}} -c {{某命令 --某参数 '其他参数内容'}}`
