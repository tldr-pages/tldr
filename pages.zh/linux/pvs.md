# pvs

> 显示有关物理卷的信息。
> 参见：`lvm`。
> 更多信息：<https://manned.org/pvs>。

- 显示物理卷的信息：

`pvs`

- 显示非物理卷：

`pvs -a`

- 改变默认显示以显示更多详情：

`pvs -v`

- 仅显示特定字段：

`pvs -o {{field_name_1}},{{field_name_2}}`

- 在默认显示中添加字段：

`pvs -o +{{field_name}}`

- 隐藏表头行：

`pvs --noheadings`

- 使用分隔符分隔字段：

`pvs --separator {{special_character}}`
