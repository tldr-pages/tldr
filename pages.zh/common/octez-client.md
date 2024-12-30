# octez-client

> 与 Tezos 区块链互动。
> 更多信息：<https://tezos.gitlab.io/introduction/howtouse.html#client>。

- 使用连接到 Tezos RPC 节点（例如 <https://rpc.ghostnet.teztnets.com>）配置客户端：

`octez-client -E {{endpoint}} config update`

- 创建一个账户并为其分配一个本地别名：

`octez-client gen keys {{alias}}`

- 通过别名或地址获取账户余额：

`octez-client get balance for {{alias_or_address}}`

- 将 tez 转移到另一个账户：

`octez-client transfer {{5}} from {{alias|address}} to {{alias|address}}`

- 发起（部署）一个智能合约，为其分配一个本地别名，并将其初始存储设置为 Michelson 编码值：

`octez-client originate contract {{alias}} transferring {{0}} from {{alias|address}} running {{path/to/source_file.tz}} --init "{{initial_storage}}" --burn_cap {{1}}`

- 通过其别名或地址调用智能合约，并传递一个 Michelson 编码的参数：

`octez-client transfer {{0}} from {{alias|address}} to {{contract}} --entrypoint "{{entrypoint}}" --arg "{{parameter}}" --burn-cap {{1}}`

- 显示帮助：

`octez-client man`