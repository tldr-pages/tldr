# input

> 将事件代码或触摸屏手势发送到 Android 设备。
> 此命令只能通过 `adb shell` 使用。
> 更多信息：<https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- 将单个字符的事件代码发送到 Android 设备：

`input keyevent {{event_code}}`

- 将文本发送到 Android 设备（`%s` 代表空格）：

`input text "{{text}}"`

- 将轻触发送到 Android 设备：

`input tap {{x_pos}} {{y_pos}}`

- 将滑动手势发送到 Android 设备：

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- 使用滑动手势将长按发送到 Android 设备：

`input swipe {{x_pos}} {{y_pos}} {{x_pos}} {{y_pos}} {{duration_in_ms}}`
