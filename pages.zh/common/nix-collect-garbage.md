# nix-收集垃圾

> 删除未使用和不可达的nix存储路径。
> 可以使用 `nix-env --list-generations` 列出代数。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>。

- 删除当前每个配置文件代数未使用的所有存储路径：

`sudo nix-collect-garbage --delete-old`

- 模拟删除旧存储路径：

`sudo nix-collect-garbage --delete-old --dry-run`

- 删除所有超过30天的存储路径：

`sudo nix-collect-garbage --delete-older-than 30d`