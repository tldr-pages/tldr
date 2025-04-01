# electrum

> 人体工学比特币钱包和个人密钥管理。
> 更多信息：<https://electrum.org>。

- 创建新钱包：

`electrum -w {{new_wallet.dat}} create`

- 离线从种子恢复现有钱包：

`electrum -w {{recovery_wallet.dat}} restore -o`

- 离线创建已签名交易：

`electrum mktx {{recipient}} {{amount}} -f 0.0000001 -F {{from}} -o`

- 显示钱包中所有接收地址：

`electrum listaddresses -a`

- 签署消息：

`electrum signmessage {{address}} {{message}}`

- 验证消息：

`electrum verifymessage {{address}} {{signature}} {{message}}`

- 仅连接到特定的 electrum 服务器实例：

`electrum -p socks5:{{127.0.0.1}}:9050 -s {{56ckl5obj37gypcu.onion}}:50001:t -1`
