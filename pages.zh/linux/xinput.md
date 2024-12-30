# xinput

> 列出可用的输入设备，查询设备信息并更改输入设备设置。
> 更多信息：<https://manned.org/xinput>。

- 列出所有输入设备：

`xinput list`

- 禁用一个输入：

`xinput disable {{id}}`

- 启用一个输入：

`xinput enable {{id}}`

- 从主设备中断开输入：

`xinput float {{id}}`

- 将输入重新附加为主设备的从设备：

`xinput reattach {{id}} {{master_id}}`

- 列出输入设备的设置：

`xinput list-props {{id}}`

- 更改输入设备的设置：

`xinput set-prop {{id}} {{setting_id}} {{value}}`