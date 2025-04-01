# cmdkey

> 创建、显示和删除存储的用户名和密码。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>。

- 列出所有用户凭证：

`cmdkey /list`

- 为访问特定服务器的用户存储凭证：

`cmdkey /add:{{server_name}} /user:{{user_name}}`

- 删除特定目标的凭证：

`cmdkey /delete {{target_name}}`