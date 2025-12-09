# cmd

> Android 服務管理器。
> 更多資訊：<https://cs.android.com/android/platform/superproject/+/main:frameworks/native/cmds/cmd/>.

- 列出所有正在執行的服務：

`cmd -l`

- 呼叫指定服務：

`cmd {{alarm}}`

- 呼叫服務同時傳遞參數：

`cmd {{vibrator}} {{vibrate 300}}`
