# lvs

> 显示逻辑卷信息。
> 另见：`lvm`.
> 更多信息：<https://man7.org/linux/man-pages/man8/lvs.8.html>.

- 显示逻辑卷信息：

`lvs`

- 显示所有逻辑卷：

`lvs -a`

- 改变默认显示以显示更多细节：

`lvs -v`

- 只显示特定字段：

`lvs -o {{域名 1}},{{域名 2}}`

- 将字段附加到显示：

`lvs -o +{{域名}}`

- 抑制标题行：

`lvs --noheadings`

- 使用特殊分隔符分隔特定字段：

`lvs --separator {{=}}`
