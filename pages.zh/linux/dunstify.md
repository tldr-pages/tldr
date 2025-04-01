# dunstify

> 通知工具，是 `notify-send` 的扩展，基于 `dunst` 提供了更多功能。
> 接受 `notify-send` 的所有选项。
> 更多信息：<https://github.com/dunst-project/dunst/wiki/Guides>.

- 显示具有指定标题和消息的通知：

`dunstify "{{标题}}" "{{消息}}"`

- 显示具有指定紧急程度的通知：

`dunstify "{{标题}}" "{{消息}}" -u {{low|normal|critical}}`

- 指定消息 ID（覆盖任何之前的具有相同 ID 的消息）：

`dunstify "{{标题}}" "{{消息}}" -r {{123}}`

- 显示帮助：

`dunstify --help`