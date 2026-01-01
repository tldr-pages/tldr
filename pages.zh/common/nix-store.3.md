# nix store

> 管理 Nix 存储。
> 另请参阅：`nix-store`。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/new-cli/nix3-store.html>。

- 收集垃圾，即删除未使用的路径以节省空间：

`nix store gc`

- 将相同的文件硬链接在一起以节省空间：

`nix store optimise`

- 删除特定的存储路径（必须是未使用的路径）：

`nix store delete /nix/store/{{校验和-包名-版本.扩展名}}`

- 列出远程存储中存储路径的内容：

`nix store --store {{https://cache.nixos.org}} ls /nix/store/{{校验和-包名-版本.扩展名}}`

- 显示两个存储路径及其依赖关系之间的版本差异：

`nix store diff-closures /nix/store/{{校验和-包名-版本.扩展名}} /nix/store/{{校验和-包名-版本.扩展名}}`