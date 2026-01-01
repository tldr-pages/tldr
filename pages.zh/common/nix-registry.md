# nix registry

> 管理 Nix 软件源注册表。
> 另请参阅：`nix flake`。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-registry.html>.

- 将 `nixpkgs` 固定到上游仓库的当前版本：

`nix registry pin {{nixpkgs}}`

- 将一个条目固定至分支的最新版本，或 GitHub 仓库的特定修订版本：

`nix registry pin {{entry}} {{github:owner/repo/branch_or_revision}}`

- 添加一个新的条目，使其始终指向 GitHub 仓库的最新版本，并能自动更新：

`nix registry add {{entry}} {{github:owner/repo}}`

- 移除一个注册表条目：

`nix registry remove {{entry}}`

- 查看关于 Nix 软件源注册表的文档说明：

`nix registry --help`
