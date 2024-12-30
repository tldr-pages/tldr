# pvs

> 显示有关物理卷的信息。
> 另见：`lvm`。
> 更多信息：<https://manned.org/pvs>。

- 显示有关物理卷的信息：

`pvs`

- 显示非物理卷：

`pvs -a`

- 更改默认显示以显示更多详细信息：

`pvs -v`

- 仅显示特定字段：

`pvs -o {{field_name_1}},{{field_name_2}}`

- 将字段附加到默认显示：

`pvs -o +{{field_name}}`

- 抑制标题行：

`pvs --noheadings`

- 使用分隔符分隔字段：

`pvs --separator {{special_character}}`