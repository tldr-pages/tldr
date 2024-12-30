# ganache-cli

> Ganache 的命令行版本，您个人的以太坊开发区块链。
> 更多信息：<https://www.trufflesuite.com/ganache>。

- 运行 Ganache：

`ganache-cli`

- 以特定数量的账户运行 Ganache：

`ganache-cli --accounts={{number_of_accounts}}`

- 以默认锁定可用账户运行 Ganache：

`ganache-cli --secure`

- 运行 Ganache 服务器并解锁特定账户：

`ganache-cli --secure --unlock "{{account_private_key1}}" --unlock "{{account_private_key2}}"`

- 以特定账户和余额运行 Ganache：

`ganache-cli --account="{{account_private_key}},{{account_balance}}"`

- 以默认余额运行 Ganache：

`ganache-cli --defaultBalanceEther={{default_balance}}`

- 运行 Ganache 并将所有请求记录到 `stdout`：

`ganache-cli --verbose`