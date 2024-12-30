# nix 注册表

> 管理 Nix flake 注册表。
> 另请参阅：有关 flakes 的信息，请参见 `nix3 flake`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-registry.html>。

- 将 `nixpkgs` 修订版固定到上游库的当前版本：

`nix registry pin {{nixpkgs}}`

- 将条目固定到分支的最新版本，或 GitHub 仓库的特定修订版：

`nix registry pin {{entry}} {{github:owner/repo/branch_or_revision}}`

- 添加一个新条目，该条目始终指向 GitHub 仓库的最新版本，并自动更新：

`nix registry add {{entry}} {{github:owner/repo}}`

- 删除注册表条目：

`nix registry remove {{entry}}`

- 查看有关 Nix flake 注册表的文档：

`nix registry --help`