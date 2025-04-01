# notify-send

> 使用当前桌面环境的通知系统创建通知。
> 更多信息：<https://manned.org/notify-send>.

- 显示标题为 "Test"，内容为 "This is a test" 的通知：

`notify-send "{{Test}}" "{{This is a test}}"`

- 显示带有自定义图标的通知：

`notify-send -i {{icon.png}} "{{Test}}" "{{This is a test}}"`

- 显示持续 5 秒的通知：

`notify-send -t 5000 "{{Test}}" "{{This is a test}}"`

- 显示带有应用程序图标和名称的通知：

`notify-send "{{Test}}" --icon={{google-chrome}} --app-name="{{Google Chrome}}"`
