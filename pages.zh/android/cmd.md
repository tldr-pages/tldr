# cmd

> Android 服务管理器。
> 更多信息：<https://cs.android.com/android/platform/superproject/+/main:frameworks/native/cmds/cmd/>.

- 列出所有正在运行的服务：

`cmd -l`

- 调用指定服务：

`cmd {{alarm}}`

- 调用服务同时传递参数：

`cmd {{vibrator}} {{vibrate 300}}`
