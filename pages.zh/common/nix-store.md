# nix-store

> 操作或查询 Nix 存储。
> 另请参见：`nix3 store`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/nix-store.html>。

- 垃圾收集，例如删除未使用的路径：

`nix-store --gc`

- 硬链接相同的文件以减少空间使用：

`nix-store --optimise`

- 删除特定的存储路径（必须未使用）：

`nix-store --delete {{/nix/store/...}}`

- 以树形格式显示存储路径（软件包）的所有依赖项：

`nix-store --query --tree {{/nix/store/...}}`

- 计算某个存储路径及其所有依赖项的总大小：

`du -cLsh $(nix-store --query --references {{/nix/store/...}})`

- 显示特定存储路径的所有引用者：

`nix-store --query --referrers {{/nix/store/...}}`