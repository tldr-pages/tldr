# lvs

> 显示逻辑卷信息。
> 另见: `lvm`。
> 更多信息参考:<https://man7.org/linux/man-pages/man8/lvs.8.html>。

- 显示逻辑卷信息
`lvs`

- 显示所有逻辑卷：
`lvs -a`

- 修改默认显示，以展示更多信息:
`lvs -v`

- 只显示特定信息域:
`lvs -o {{field_name_1}},{{field_name_2}}`

- 附加域到默认展示：
`lvs -o +{{field_name}}`

- 取缔标题线:
`lvs --noheadings`

- 使用指定分隔符分隔域:
`lvs --separator {{=}}`
