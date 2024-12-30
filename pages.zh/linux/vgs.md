# vgs

> 显示卷组的信息。
> 参见：`lvm`。
> 更多信息：<https://manned.org/vgs>。

- 显示卷组的信息：

`vgs`

- 显示所有卷组：

`vgs -a`

- 更改默认显示以显示更多详细信息：

`vgs -v`

- 仅显示特定字段：

`vgs -o {{field_name_1}},{{field_name_2}}`

- 将字段附加到默认显示：

`vgs -o +{{field_name}}`

- 抑制标题行：

`vgs --noheadings`

- 使用分隔符来分隔字段：

`vgs --separator =`