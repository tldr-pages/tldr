# hsd-cli

> 适用于 Handshake 区块链的命令行 REST 工具。
> 更多信息：<https://handshake.org>.

- 获取当前服务器的信息：

`hsd-cli info`

- 广播本地交易：

`hsd-cli broadcast {{transaction_hex}}`

- 获取内存池快照：

`hsd-cli mempool`

- 通过地址或哈希查看交易：

`hsd-cli tx {{address_or_hash}}`

- 通过哈希索引或地址查看币：

`hsd-cli coin {{hash_index_or_address}}`

- 通过高度或哈希查看区块：

`hsd-cli block {{height_or_hash}}`

- 将链重置到指定的区块：

`hsd-cli reset {{height_or_hash}}`

- 执行 RPC 命令：

`hsd-cli rpc {{command}} {{args}}`
