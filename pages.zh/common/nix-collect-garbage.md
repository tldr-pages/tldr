# nix-collect-garbage

> 删除未使用且不可达的 Nix 存储路径。
> 可以使用 `nix-env --list-generations` 列出生成。
> 更多信息：<https://nixos.org/manual/nix/stable/command-ref/nix-collect-garbage.html>.

- 删除每个配置文件当前生成未使用的存储路径：

`sudo nix-collect-garbage --delete-old`

- 模拟删除旧的存储路径：

`sudo nix-collect-garbage --delete-old --dry-run`

- 删除所有超过 30 天的存储路径：

`sudo nix-collect-garbage --delete-older-than 30d`
