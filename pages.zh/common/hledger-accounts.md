# hledger accounts

> 列出账户名称。
> 更多信息：<https://hledger.org/hledger.html#accounts>。

- 显示默认日记文件中使用或声明的所有账户：

`hledger accounts`

- 显示交易中使用的账户：

`hledger accounts --used`

- 显示用账户指令声明的账户：

`hledger accounts --declared`

- 为使用但未声明的账户添加新的账户指令到日记文件中：

`hledger accounts --undeclared --directives >> {{2024-accounts.journal}}`

- 显示名称中包含 `asset` 的账户及其声明或推断的类型：

`hledger accounts asset --types`

- 显示 `Asset` 类型的账户：

`hledger accounts type:A`

- 显示账户层次结构的前两级：

`hledger accounts --tree --depth 2`

- 上述命令的简写形式：

`hledger acc -t -2`
