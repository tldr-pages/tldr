# nix store

> 操作 Nix 存储。
> 另见: `nix-store`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-store.html>。

- 收集垃圾，即删除未使用的路径以减少磁盘空间占用：

`nix store gc`

- 将相同的文件硬链接在一起以减少磁盘空间占用：

`nix store optimise`

- 删除特定的存储路径（必须未被使用）：

`nix store delete {{/nix/store/...}}`

- 列出远程存储路径的内容：

`nix store --store {{https://cache.nixos.org}} ls {{/nix/store/...}}`

- 显示两个存储路径及其各自依赖项之间的版本差异：

`nix store diff-closures {{/nix/store/...}} {{/nix/store/...}}`