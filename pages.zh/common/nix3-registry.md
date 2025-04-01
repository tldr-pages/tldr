# nix registry

> 管理 Nix flake 注册表。
> 更多信息参见: `nix3 flake` 了解关于 flakes 的信息。
> 更多信息: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-registry.html>。

- 将 `nixpkgs` 版本固定为上游仓库的当前版本：

`nix registry pin {{nixpkgs}}`

- 将条目固定为 GitHub 仓库分支的最新版本或特定修订版本：

`nix registry pin {{entry}} {{github:owner/repo/branch_or_revision}}`

- 添加一个新的条目，该条目始终指向 GitHub 仓库的最新版本，并自动更新：

`nix registry add {{entry}} {{github:owner/repo}}`

- 移除注册表中的条目：

`nix registry remove {{entry}}`

- 查看关于 Nix flake 注册表的文档：

`nix registry --help`
