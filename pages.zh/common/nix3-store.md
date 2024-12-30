# nix 存储

> 操作 Nix 存储。
> 另见：`nix-store`。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-store.html>。

- 垃圾回收，即删除未使用的路径以减少空间使用：

`nix store gc`

- 硬链接相同的文件以减少空间使用：

`nix store optimise`

- 删除特定的存储路径（必须未使用）：

`nix store delete {{/nix/store/...}}`

- 列出远程存储的存储路径的内容：

`nix store --store {{https://cache.nixos.org}} ls {{/nix/store/...}}`

- 显示两个存储路径之间版本的差异及其各自的依赖关系：

`nix store diff-closures {{/nix/store/...}} {{/nix/store/...}}`