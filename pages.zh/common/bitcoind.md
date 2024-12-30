# bitcoind

> Bitcoin Core 守护进程。
> 使用 `bitcoin.conf` 中定义的配置。
> 更多信息：<https://manned.org/bitcoind>。

- 启动 Bitcoin Core 守护进程（在前台）：

`bitcoind`

- 在后台启动 Bitcoin Core 守护进程（使用 `bitcoin-cli stop` 停止）：

`bitcoind -daemon`

- 在特定网络上启动 Bitcoin Core 守护进程：

`bitcoind -chain={{main|test|signet|regtest}}`

- 使用特定配置文件和数据目录启动 Bitcoin Core 守护进程：

`bitcoind -conf={{path/to/bitcoin.conf}} -datadir={{path/to/directory}}`