# hledger aregister

> 显示一个账户中的交易和当前余额，每笔交易占一行。
> 更多信息：<https://hledger.org/hledger.html#aregister>。

- 显示 `assets:bank:checking` 账户中的交易和当前余额：

`hledger aregister assets:bank:checking`

- 显示名为 `*savings*` 的第一个账户中的交易和当前余额：

`hledger aregister savings`

- 显示 checking 账户的已清算交易，并指定宽度：

`hledger aregister checking --cleared --width {{120}}`

- 显示 checking 账户的交易记录，包括来自预测规则的交易：

`hledger aregister checking --forecast`