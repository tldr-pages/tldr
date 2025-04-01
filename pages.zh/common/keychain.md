# keychain

> 在登录之间重用 ssh-agent 和/或 gpg-agent。
> 更多信息：<https://funtoo.org/Keychain>。

- 检查是否有正在运行的 ssh-agent，需要时启动一个：

`keychain`

- 同时检查 gpg-agent：

`keychain --agents "{{gpg,ssh}}"`

- 列出所有活跃密钥的签名：

`keychain --list`

- 列出所有活跃密钥的指纹：

`keychain --list-fp`

- 为添加到代理的身份设置超时时间，以分钟为单位：

`keychain --timeout {{minutes}}`
