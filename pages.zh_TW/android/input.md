# input

> 將事件代碼或觸控螢幕手勢傳送到 Android 裝置。
> 此命令只能透過 `adb shell` 使用。
> 更多資訊：<https://developer.android.com/reference/android/view/KeyEvent.html#constants_1>.

- 將單個字元的事件代碼傳送到 Android 裝置：

`input keyevent {{事件代碼}}`

- 將文字傳送到 Android 裝置（`%s` 代表空格）：

`input text "{{文字}}"`

- 將輕觸發送到 Android 裝置：

`input tap {{x 值}} {{y 值}}`

- 將滑動手勢傳送到 Android 裝置：

`input swipe {{x 開始值}} {{y 開始值}} {{x 結束值}} {{y 結束值}} {{持續時間（微秒）}}`

- 使用滑動手勢將長按傳送到 Android 裝置：

`input swipe {{x 值}} {{y 值}} {{x 值}} {{y 值}} {{持續時間（微秒）}}`
