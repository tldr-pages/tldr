# nologin

> 用于防止用户登录的替代 shell。
> 更多信息：<https://manned.org/nologin.5>.

- 将用户的登录 shell 设置为 `nologin` 以防止用户登录：

`chsh {{[-s|--shell]}} {{user}} nologin`

- 自定义 `nologin` 登录 shell 用户的消息：

`echo "{{拒绝登录消息}}" > /etc/nologin.txt`