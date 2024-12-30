# lvs

> 显示有关逻辑卷的信息。
> 另见：`lvm`。
> 更多信息：<https://manned.org/lvs>。

- 显示有关逻辑卷的信息：

`lvs`

- 显示所有逻辑卷：

`lvs -a`

- 更改默认显示以显示更多详细信息：

`lvs -v`

- 仅显示特定字段：

`lvs -o {{field_name_1}},{{field_name_2}}`

- 将字段附加到默认显示：

`lvs -o +{{field_name}}`

- 抑制标题行：

`lvs --noheadings`

- 使用分隔符分隔字段：

`lvs --separator {{=}}`