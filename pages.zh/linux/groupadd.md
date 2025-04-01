# groupadd

> 向系统中添加用户组。
> 参见：`groups`，`groupdel`，`groupmod`。
> 更多信息：<https://manned.org/groupadd>。

- 创建一个新用户组：

`sudo groupadd {{group_name}}`

- 创建一个新的系统用户组：

`sudo groupadd {{[-r|--system]}} {{group_name}}`

- 创建一个具有特定组ID的新用户组：

`sudo groupadd {{[-g|--gid]}} {{id}} {{group_name}}`
