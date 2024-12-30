# nologin

> 替代的 shell，防止用户登录。
> 更多信息：<https://manned.org/nologin.5>。

- 将用户的登录 shell 设置为 `nologin` 以防止用户登录：

`chsh -s {{user}} nologin`

- 自定义登录 shell 为 `nologin` 的用户的消息：

`echo "{{declined_login_message}}" > /etc/nologin.txt`