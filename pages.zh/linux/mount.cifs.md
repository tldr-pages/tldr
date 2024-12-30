# mount.cifs

> 挂载 SMB（服务器消息块）或 CIFS（通用互联网文件系统）共享。
> 注意：您也可以通过将 `-t cifs` 选项传递给 `mount` 来完成相同的操作。
> 更多信息：<https://manned.org/mount.cifs>。

- 使用指定的用户名或默认的 `$USER` 连接（系统会提示您输入密码）：

`mount.cifs -o user={{username}} //{{server}}/{{share_name}} {{mountpoint}}`

- 以访客用户身份连接（不需要密码）：

`mount.cifs -o guest //{{server}}/{{share_name}} {{mountpoint}}`

- 设置挂载目录的所有权信息：

`mount.cifs -o uid={{user_id|username}},gid={{group_id|groupname}} //{{server}}/{{share_name}} {{mountpoint}}`