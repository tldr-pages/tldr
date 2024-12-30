# vgremove

> 在LVM中移除卷组。
> 更多信息：<https://manned.org/vgremove>。

- 移除卷组并要求确认：

`vgremove {{volume_group}}`

- 强制移除卷组而不要求确认：

`vgremove --force {{volume_group}}`

- 将调试级别设置为详细日志记录的级别2（重复`--debug`最多6次以增加级别）：

`vgremove --debug --debug {{volume_group}}`

- 使用特定的配置设置以覆盖默认值：

`vgremove --config '{{global/locking_type=1}}' {{volume_group}}`

- 显示用法信息的帮助文本：

`vgremove --help`