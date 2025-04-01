# edquota

> 编辑用户或组的磁盘配额。默认情况下，它会操作所有设置了配额的文件系统。
> 配额信息永久存储在文件系统根目录下的 `quota.user` 和 `quota.group` 文件中。
> 更多信息：<https://manned.org/edquota>.

- 编辑当前用户的配额：

`edquota --user $(whoami)`

- 编辑特定用户的配额：

`sudo edquota --user {{username}}`

- 编辑组的配额：

`sudo edquota --group {{group}}`

- 限制操作到指定的文件系统（默认情况下 edquota 会操作所有设置了配额的文件系统）：

`sudo edquota --file-system {{filesystem}}`

- 编辑默认的宽限期：

`sudo edquota -t`

- 复制配额到其他用户：

`sudo edquota -p {{reference_user}} {{destination_user1}} {{destination_user2}}`