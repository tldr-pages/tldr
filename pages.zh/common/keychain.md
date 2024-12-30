# 密钥链

> 在登录之间重复使用 ssh-agent 和/或 gpg-agent。
> 更多信息：<https://funtoo.org/Keychain>。

- 检查是否有正在运行的 ssh-agent，如果需要则启动一个：

`keychain`

- 还要检查 gpg-agent：

`keychain --agents "{{gpg,ssh}}"`

- 列出所有活动密钥的签名：

`keychain --list`

- 列出所有活动密钥的指纹：

`keychain --list-fp`

- 为添加到代理的身份设置超时（以分钟为单位）：

`keychain --timeout {{分钟}}`