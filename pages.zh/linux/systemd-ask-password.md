# systemd-ask-password

> 请求用户输入系统密码。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-ask-password.html>。

- 使用特定提示请求系统密码：

`systemd-ask-password "{{prompt}}"`

- 为密码请求指定一个标识符：

`systemd-ask-password --id {{identifier}} "{{prompt}}"`

- 使用内核密钥环密钥名称作为密码的缓存：

`systemd-ask-password --keyname {{key_name}} "{{prompt}}"`

- 为密码请求设置自定义超时时间：

`systemd-ask-password --timeout {{seconds}} "{{prompt}}"`

- 强制使用代理系统，从不在当前 TTY 上请求密码：

`systemd-ask-password --no-tty "{{prompt}}"`

- 将密码存储在内核密钥环中而不显示密码：

`systemd-ask-password --no-output --keyname {{key_name}} "{{prompt}}"`

- 将请求的密码传递给另一个程序：

`systemd-ask-password | {{command}}`

- 显示帮助信息：

`systemd-ask-password {{[-h|--help]}}`
