# 输入

> 将事件代码或触摸屏手势发送到 Android 设备。
> 此命令只能通过 `adb shell` 使用。
> 更多信息：<https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>。

- 将单个字符的事件代码发送到 Android 设备：

`input keyevent {{event_code}}`

- 向 Android 设备发送文本（`%s` 代表空格）：

`input text "{{text}}"`

- 向 Android 设备发送单次点击：

`input tap {{x_position}} {{y_position}}`

- 向 Android 设备发送滑动手势：

`input swipe {{x_start}} {{y_start}} {{x_end}} {{y_end}} {{duration_in_ms}}`

- 使用滑动手势向 Android 设备发送长按：

`input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{duration_in_ms}}`