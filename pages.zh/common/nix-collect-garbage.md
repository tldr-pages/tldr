# nix-collect-garbage

> 删除未使用且不可访问的 nix 存储路径。
> 可通过 `nix-env --list-generations` 查看各代配置。
> 更多信息：<https://nix.dev/manual/nix/stable/command-ref/nix-collect-garbage.html>.

- 删除与用户相关、未被当前各配置代次使用的所有存储路径：

`nix-collect-garbage {{[-d|--delete-old]}}`

- 模拟删除旧的存储路径（仅展示可删除项）：

`nix-collect-garbage {{[-d|--delete-old]}} --dry-run`

- 删除所有创建时间超过 30 天的存储路径：

`nix-collect-garbage --delete-older-than 30d`

- 系统范围内删除各配置当前代次未使用的所有存储路径（需管理员权限）：

`sudo nix-collect-garbage {{[-d|--delete-old]}}`
