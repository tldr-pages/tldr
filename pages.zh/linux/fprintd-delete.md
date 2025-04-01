# fprintd-delete

> 从数据库中删除指纹。
> 更多信息：<https://manned.org/fprintd-delete>.

- 删除指定用户的全部指纹：

`fprintd-delete {{username}}`

- 删除指定用户的特定指纹：

`fprintd-delete {{username}} --finger {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger}}`

- 显示帮助信息：

`fprintd-delete`
