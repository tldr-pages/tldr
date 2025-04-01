# sui client

> 发布智能合约，获取对象信息，执行交易等。
> 更多信息：<https://docs.sui.io/references/cli/client>.

- 使用 ED25519 方案创建新地址：

`sui client new-address ed25519 {{address-alias}}`

- 使用 RPC URL 和别名创建新的测试网络环境：

`sui client new-env --rpc https://fullnode.testnet.sui.io:443 --alias testnet`

- 切换到指定的地址（也接受别名）：

`sui client switch --address {{address-alias}}`

- 切换到指定的环境：

`sui client switch --env {{env-alias}}`

- 发布智能合约：

`sui client publish {{package-path}}`

- 与 Sui 水龙头互动：

`sui client faucet {{subcommand}}`

- 列出指定地址的 GAS 代币（也接受别名）：

`sui client gas {{address}}`

- 创建、签署和执行可编程交易块：

`sui client ptb {{options}} {{subcommand}}`