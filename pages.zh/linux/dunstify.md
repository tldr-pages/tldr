# dunstify

> 一种通知工具，是 `notify-send` 的扩展，具有更多围绕 `dunst` 的功能。
> 接受所有 `notify-send` 的选项。
> 更多信息：<https://github.com/dunst-project/dunst/wiki/Guides>。

- 显示带有指定标题和消息的通知：

`dunstify "{{Title}}" "{{Message}}"`

- 显示具有指定紧迫性的通知：

`dunstify "{{Title}}" "{{Message}}" -u {{low|normal|critical}}`

- 指定消息 ID（覆盖任何先前相同 ID 的消息）：

`dunstify "{{Title}}" "{{Message}}" -r {{123}}`

- 显示帮助信息：

`dunstify --help`