# ganache-cli

> Ganache 的命令行版本，用于 Ethereum 开发的个人区块链。
> 更多信息：<https://www.trufflesuite.com/ganache>。

- 运行 Ganache：

`ganache-cli`

- 使用指定数量的账户运行 Ganache：

`ganache-cli --accounts={{number_of_accounts}}`

- 运行 Ganache 并默认锁定所有可用账户：

`ganache-cli --secure`

- 运行 Ganache 服务器并解锁指定账户：

`ganache-cli --secure --unlock "{{account_private_key1}}" --unlock "{{account_private_key2}}"`

- 使用指定账户和余额运行 Ganache：

`ganache-cli --account="{{account_private_key}},{{account_balance}}"`

- 运行 Ganache，账户设置默认余额：

`ganache-cli --defaultBalanceEther={{default_balance}}`

- 运行 Ganache 并将所有请求记录到 `stdout`：

`ganache-cli --verbose`