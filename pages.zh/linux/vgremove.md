# vgremove

> 在 LVM 中移除卷组。
> 更多信息：<https://manned.org/vgremove>。

- 移除卷组，并要求确认：

`vgremove {{卷组}}`

- 强制移除卷组，无需确认：

`vgremove --force {{卷组}}`

- 将调试级别设置为 2，以获取详细日志（最多重复 `--debug` 6 次以提高级别）：

`vgremove --debug --debug {{卷组}}`

- 使用特定配置设置覆盖默认设置：

`vgremove --config '{{global/locking_type=1}}' {{卷组}}`

- 显示帮助文本以获取使用信息：

`vgremove --help`