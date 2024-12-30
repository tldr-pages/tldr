# groupadd

> 向系统添加用户组。
> 另见：`groups`、`groupdel`、`groupmod`。
> 更多信息：<https://manned.org/groupadd>。

- 创建一个新组：

`sudo groupadd {{group_name}}`

- 创建一个新的系统组：

`sudo groupadd --system {{group_name}}`

- 使用特定的组ID创建一个新组：

`sudo groupadd --gid {{id}} {{group_name}}`