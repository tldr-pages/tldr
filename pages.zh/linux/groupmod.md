# groupmod

> 修改系统中现有的用户组。
> 另见：`groups`，`groupadd`，`groupdel`。
> 更多信息：<https://manned.org/groupmod>。

- 修改组名称：

`sudo groupmod --new-name {{new_group}} {{group_name}}`

- 修改组ID：

`sudo groupmod --gid {{new_id}} {{group_name}}`