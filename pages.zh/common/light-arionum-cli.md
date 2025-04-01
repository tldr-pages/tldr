# light-arionum-cli

> 用于 Arionum 加密货币的 PHP 轻量级钱包。
> 更多信息：<https://github.com/arionum/lightWalletCLI>。

- 生成一个新的公钥/私钥对：

`light-arionum-cli`

- 显示当前地址的余额：

`light-arionum-cli balance`

- 显示指定地址的余额：

`light-arionum-cli balance {{address}}`

- 发送交易，可附带可选消息：

`light-arionum-cli send {{address}} {{value}} {{optional_message}}`

- 导出当前钱包信息：

`light-arionum-cli export`

- 显示当前区块的信息：

`light-arionum-cli block`

- 显示当前地址的交易信息：

`light-arionum-cli transactions`

- 显示特定交易的信息：

`light-arionum-cli transaction {{transaction_id}}`