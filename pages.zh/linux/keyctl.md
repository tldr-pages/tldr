# keyctl

> 操作 Linux 内核密钥环。
> 更多信息: <https://manned.org/keyctl>。

- 列出特定密钥环中的密钥：

`keyctl list {{target_keyring}}`

- 列出用户默认会话中的当前密钥：

`keyctl list {{@us}}`

- 在特定密钥环中存储一个密钥：

`keyctl add {{type_keyring}} {{key_name}} {{key_value}} {{target_keyring}}`

- 从 `stdin` 存储一个密钥及其值：

`echo -n {{key_value}} | keyctl padd {{type_keyring}} {{key_name}} {{target_keyring}}`

- 为密钥设置超时：

`keyctl timeout {{key_name}} {{timeout_in_seconds}}`

- 读取密钥并在不可打印时格式化为十六进制转储：

`keyctl read {{key_name}}`

- 读取密钥并按原样格式化：

`keyctl pipe {{key_name}}`

- 撤销一个密钥并防止对其进行任何进一步操作：

`keyctl revoke {{key_name}}`