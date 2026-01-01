# nix-store

> 操作或查询 Nix 存储。
> 另请参阅：`nix store.3`。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/nix-store.html>。

- 执行垃圾回收，比如删除未使用的路径：

`nix-store --gc`

- 将相同的文件硬链接到一起以节省空间：

`nix-store --optimise`

- 删除特定的存储路径（必须未在使用中）：

`nix-store --delete /nix/store/{{checksum-package-version.ext}}`

- 以树状格式显示存储路径（包）的所有依赖关系：

`nix-store {{[-q|--query]}} --tree /nix/store/{{checksum-package-version.ext}}`

- 计算某个存储路径及其所有依赖关系的总大小：

`du {{[-cLsh|--total --dereference --summarize --human-readable]}} $(nix-store {{[-q|--query]}} --references /nix/store/{{checksum-package-version.ext}})`

- 显示特定存储路径的所有依赖项：

`nix-store {{[-q|--query]}} --referrers /nix/store/{{checksum-package-version.ext}}`

