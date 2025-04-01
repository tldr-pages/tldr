# sic

> 简单的 IRC 客户端。
> suckless 工具集的一部分。
> 更多信息：<https://tools.suckless.org/sic/>.

- 使用 `$USER` 环境变量中设置的昵称连接到默认主机（irc.ofct.net）：

`sic`

- 使用指定的昵称连接到指定的主机：

`sic -h {{host}} -n {{nickname}}`

- 使用指定的昵称和密码连接到指定的主机：

`sic -h {{host}} -n {{nickname}} -k {{password}}`

- 加入频道：

`:j #{{channel}}<Enter>`

- 向频道或用户发送消息：

`:m #{{channel|user}}<Enter>`

- 设置默认频道或用户：

`:s #{{channel|user}}<Enter>`
