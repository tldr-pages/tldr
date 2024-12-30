# gcalcli

> 与谷歌日历互动。
> 首次启动时请求谷歌API授权。
> 更多信息：<https://github.com/insanum/gcalcli>。

- 列出您所有日历在接下来的7天内的事件：

`gcalcli agenda`

- 显示从特定日期起或特定日期之间的事件（也可以使用相对日期，例如“明天”）：

`gcalcli agenda {{mm/dd}} [{{mm/dd}}]`

- 列出特定日历中的事件：

`gcalcli --calendar {{calendar_name}} agenda`

- 按周显示事件的ASCII日历：

`gcalcli calw`

- 按月显示事件的ASCII日历：

`gcalcli calm`

- 快速添加事件到您的日历：

`gcalcli --calendar {{calendar_name}} quick "{{mm/dd}} {{HH:MM}} {{event_name}}"`

- 向日历添加事件。触发互动提示：

`gcalcli --calendar "{{calendar_name}}" add`