# gcalcli

> 与 Google 日历交互。
> 首次启动时会请求 Google API 授权。
> 更多信息：<https://github.com/insanum/gcalcli>。

- 列出所有日历中未来 7 天内的事件：

`gcalcli agenda`

- 显示从特定日期开始或在特定日期之间的事件（也接受相对日期，例如 "tomorrow"）：

`gcalcli agenda {{mm/dd}} [{{mm/dd}}]`

- 列出特定日历中的事件：

`gcalcli --calendar {{calendar_name}} agenda`

- 以周为单位显示事件的 ASCII 日历：

`gcalcli calw`

- 以月为单位显示事件的 ASCII 日历：

`gcalcli calm`

- 快速向日历中添加事件：

`gcalcli --calendar {{calendar_name}} quick "{{mm/dd}} {{HH:MM}} {{event_name}}"`

- 向日历中添加事件。触发交互式提示：

`gcalcli --calendar "{{calendar_name}}" add`