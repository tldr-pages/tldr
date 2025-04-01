# hsw-cli

> Handshake 钱包的命令行 REST 工具。
> 更多信息：<https://github.com/handshake-org/hs-client>.

- 解锁当前钱包（超时时间以秒为单位）：

`hsw-cli unlock {{passphrase}} {{timeout}}`

- 锁定当前钱包：

`hsw-cli lock`

- 查看当前钱包的详细信息：

`hsw-cli get`

- 查看当前钱包的余额：

`hsw-cli balance`

- 查看当前钱包的交易历史：

`hsw-cli history`

- 向指定地址发送指定数量的币：

`hsw-cli send {{address}} {{1.05}}`

- 查看当前钱包的未确认交易：

`hsw-cli pending`

- 查看交易的详细信息：

`hsw-cli tx {{transaction_hash}}`
