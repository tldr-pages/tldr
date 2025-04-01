# mount.cifs

> 挂载 SMB（Server Message Block）或 CIFS（Common Internet File System）共享。
> 注意：您也可以通过向 `mount` 传递 `-t cifs` 选项来完成相同的操作。
> 更多信息：<https://manned.org/mount.cifs>.

- 使用指定的用户名或默认使用 `$USER` 连接（您将被提示输入密码）：

`mount.cifs -o user={{username}} //{{server}}/{{share_name}} {{mountpoint}}`

- 以访客用户身份连接（无需密码）：

`mount.cifs -o guest //{{server}}/{{share_name}} {{mountpoint}}`

- 为挂载目录设置所有权信息：

`mount.cifs -o uid={{user_id|username}},gid={{group_id|groupname}} //{{server}}/{{share_name}} {{mountpoint}}`