# edquota

> 编辑用户或组的配额。默认情况下，它在所有具有配额的文件系统上操作。
> 配额信息永久存储在文件系统根目录下的 `quota.user` 和 `quota.group` 文件中。
> 更多信息：<https://manned.org/edquota>。

- 编辑当前用户的配额：

`edquota --user $(whoami)`

- 编辑特定用户的配额：

`sudo edquota --user {{username}}`

- 编辑某个组的配额：

`sudo edquota --group {{group}}`

- 将操作限制在给定的文件系统上（默认情况下，edquota 在所有具有配额的文件系统上操作）：

`sudo edquota --file-system {{filesystem}}`

- 编辑默认宽限期：

`sudo edquota -t`

- 将配额复制到其他用户：

`sudo edquota -p {{reference_user}} {{destination_user1}} {{destination_user2}}`