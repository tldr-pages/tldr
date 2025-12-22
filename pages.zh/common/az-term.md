# az term

> 使用 marketplaceordering 管理市场条款。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/term>.

- 打印市场条款：

`az term show --product "{{产品标识符}}" --plan "{{计划标识符}}" --publisher "{{发布者标识符}}"`

- 接受市场条款：

`az term accept --product "{{产品标识符}}" --plan "{{计划标识符}}" --publisher "{{发布者标识符}}"`
