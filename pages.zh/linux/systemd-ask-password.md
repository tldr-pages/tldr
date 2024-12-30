# systemd-ask-password

> 查询用户的系统密码。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-ask-password.html>。

- 使用特定消息查询系统密码：

`systemd-ask-password "{{message}}"`

- 为密码查询指定一个标识符：

`systemd-ask-password --id={{identifier}} "{{message}}"`

- 使用内核密钥环的密钥名称作为密码的缓存：

`systemd-ask-password --keyname={{key_name}} "{{message}}"`

- 为密码查询设置自定义超时：

`systemd-ask-password --timeout={{seconds}} "{{message}}"`

- 强制使用代理系统，并且不在当前TTY上询问：

`systemd-ask-password --no-tty "{{message}}"`

- 在不显示密码的情况下将密码存储在内核密钥环中：

`systemd-ask-password --no-output --keyname={{key_name}} "{{message}}"`
