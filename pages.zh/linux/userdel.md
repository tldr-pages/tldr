# userdel

> 删除用户账户或从组中删除用户。
> 参见：`users`, `useradd`, `usermod`。
> 更多信息：<https://manned.org/userdel>.

- 删除用户：

`sudo userdel {{username}}`

- 在其他根目录中删除用户：

`sudo userdel {{[-R|--root]}} {{path/to/other/root}} {{username}}`

- 删除用户的同时删除其家目录和邮件队列：

`sudo userdel {{[-r|--remove]}} {{username}}`
