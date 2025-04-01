# bitcoin-cli

> 用于通过 RPC 调用与 Bitcoin Core 守护进程进行交互的命令行客户端。
> 使用在 `bitcoin.conf` 中定义的配置。
> 更多信息：<https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>。

- 向指定地址发送交易：

`bitcoin-cli sendtoaddress "{{address}}" {{amount}}`

- 生成一个或多个区块：

`bitcoin-cli generate {{num_blocks}}`

- 打印钱包的高级信息：

`bitcoin-cli getwalletinfo`

- 列出所有可用来资助外出交易的前序交易输出：

`bitcoin-cli listunspent`

- 将钱包信息导出到文本文件：

`bitcoin-cli dumpwallet "{{path/to/file}}"`

- 获取区块链信息：

`bitcoin-cli getblockchaininfo`

- 获取网络信息：

`bitcoin-cli getnetworkinfo`

- 停止 Bitcoin Core 守护进程：

`bitcoin-cli stop`