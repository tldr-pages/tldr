# az term

> 管理与 marketplaceordering 的市场协议。
> 这是 `azure-cli` （也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/term>。

- 打印市场条款：

`az term show --product "{{product_identifier}}" --plan "{{plan_identifier}}" --publisher "{{publisher_identifier}}"`

- 接受市场条款：

`az term accept --product "{{product_identifier}}" --plan "{{plan_identifier}}" --publisher "{{publisher_identifier}}"`