# lpass

> LastPass 密码管理器的命令行界面。
> 更多信息：<https://github.com/lastpass/lastpass-cli>。

- 通过输入主密码登录 LastPass 账户：

`lpass login {{username}}`

- 显示登录状态：

`lpass status`

- 列出按类别分组的所有站点：

`lpass ls`

- 为 gmail.com 生成一个新密码，标识符为 `myinbox`，并添加到 LastPass：

`lpass generate --username {{username}} --url {{gmail.com}} {{myinbox}} {{password_length}}`

- 显示指定条目的密码：

`lpass show {{myinbox}} --password`
