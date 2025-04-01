# mytop

> 显示 MySQL 服务器的性能信息，类似于 `top` 命令。
> 更多信息：<https://jeremy.zawodny.com/mysql/mytop/mytop.html>.

- 启动 `mytop`：

`mytop`

- 使用指定的用户名和密码连接：

`mytop -u {{user}} -p {{password}}`

- 使用指定的用户名连接（系统会提示输入密码）：

`mytop -u {{user}} --prompt`

- 不显示任何空闲（休眠）线程：

`mytop -u {{user}} -p {{password}} --noidle`