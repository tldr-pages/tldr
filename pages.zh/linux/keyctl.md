# keyctl

> 操控 Linux 内核密钥环。
> 更多信息：<https://manned.org/keyctl>.

- 列出指定密钥环中的密钥：

`keyctl list {{target_keyring}}`

- 列出用户默认会话中的当前密钥：

`keyctl list {{@us}}`

- 在指定密钥环中存储密钥：

`keyctl add {{type_keyring}} {{key_name}} {{key_value}} {{target_keyring}}`

- 从 `stdin` 读取密钥值并存储：

`echo -n {{key_value}} | keyctl padd {{type_keyring}} {{key_name}} {{target_keyring}}`

- 为密钥设置超时时间：

`keyctl timeout {{key_name}} {{timeout_in_seconds}}`

- 读取密钥，如果密钥内容不可打印则以十六进制格式显示：

`keyctl read {{key_name}}`

- 读取密钥，不进行格式转换：

`keyctl pipe {{key_name}}`

- 撤销密钥，防止进一步操作：

`keyctl revoke {{key_name}}`