# nix-store

> 操作或查询 Nix 存储。
> 参见：`nix3 store`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/nix-store.html>。

- 收集垃圾，例如删除未使用的路径：

`nix-store --gc`

- 通过硬链接相同文件来减少磁盘使用：

`nix-store --optimise`

- 删除特定的存储路径（必须未被使用）：

`nix-store --delete {{/nix/store/...}}`

- 以树状格式显示存储路径（包）的所有依赖项：

`nix-store --query --tree {{/nix/store/...}}`

- 计算特定存储路径及其所有依赖项的总大小：

`du -cLsh $(nix-store --query --references {{/nix/store/...}})`

- 显示特定存储路径的所有依赖者：

`nix-store --query --referrers {{/nix/store/...}}`
