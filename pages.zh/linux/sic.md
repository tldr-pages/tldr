# sic

> 简单的IRC客户端。
> 属于suckless工具的一部分。
> 更多信息：<https://tools.suckless.org/sic/>.

- 使用在`$USER`环境变量中设置的昵称连接到默认主机（irc.ofct.net）：

`sic`

- 使用给定的主机和昵称连接：

`sic -h {{host}} -n {{nickname}}`

- 使用给定的主机、昵称和密码连接：

`sic -h {{host}} -n {{nickname}} -k {{password}}`

- 加入一个频道：

`:j #{{channel}}<Enter>`

- 发送消息到一个频道或用户：

`:m #{{channel|user}}<Enter>`

- 设置默认频道或用户：

`:s #{{channel|user}}<Enter>`