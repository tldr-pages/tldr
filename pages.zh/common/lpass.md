# lpass

> LastPass 密码管理器的命令行界面。
> 更多信息：<https://github.com/lastpass/lastpass-cli>。

- 登录到您的 LastPass 账户，按照提示输入您的主密码：

`lpass login {{用户名}}`

- 显示登录状态：

`lpass status`

- 按类别列出所有网站：

`lpass ls`

- 为 gmail.com 生成一个新密码，标识符为 `myinbox` 并添加到 LastPass：

`lpass generate --username {{用户名}} --url {{gmail.com}} {{myinbox}} {{密码长度}}`

- 显示指定条目的密码：

`lpass show {{myinbox}} --password`