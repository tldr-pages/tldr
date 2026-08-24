# lvs

> 显示逻辑卷信息。
> 另请参阅：`lvm`。
> 更多信息：<https://manned.org/lvs>。

- 显示逻辑卷信息：

`sudo lvs`

- 显示所有逻辑卷：

`sudo lvs {{[-a|--all]}}`

- 改变默认显示以显示更多细节：

`sudo lvs {{[-v|--verbose]}}`

- 只显示特定字段：

`sudo lvs {{[-o|--options]}} {{域名 1,域名 2,...}}`

- 将字段附加到显示：

`sudo lvs {{[-o|--options]}} +{{域名}}`

- 抑制标题行：

`sudo lvs --noheadings`

- 使用特殊分隔符分隔特定字段：

`sudo lvs --separator {{=}}`
