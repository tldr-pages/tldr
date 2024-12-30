# userdel

> 删除用户帐户或将用户从组中移除。
> 另见：`users`，`useradd`，`usermod`。
> 更多信息：<https://manned.org/userdel>。

- 删除用户：

`sudo userdel {{用户名}}`

- 在其他根目录中删除用户：

`sudo userdel {{-R|--root}} {{其他/根/路径}} {{用户名}}`

- 删除用户及其主目录和邮件库：

`sudo userdel {{-r|--remove}} {{用户名}}`