# adb-logcat

> 转储系统消息日志。
> 更多信息：<https://developer.android.com/tools/logcat>.

- 显示系统日志：

`adb logcat`

- 显示符合正则表达式的行：

`adb logcat -e {{正则表达式}}`

- 显示特定优先级下（V：详细，D：调试，I：信息，W：警告，E：错误，F：严重错误，S：静默）标记的日志，过滤掉其他标记：

`adb logcat {{标记}}:{{最低优先级}} *:S`

- 在详细（V）模式下显示 React Native 应用程序的日志，静默（S）其他标记：

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- 显示优先级为警告（W）及以上的所有标签的日志：

`adb logcat *:W`

- 显示特定 PID 的日志：

`adb logcat --pid={{pid}}`

- 显示某个特定软件包的进程日志：

`adb logcat --pid=$(adb shell pidof -s {{软件包}})`

- 给日志着色（通常与过滤器一起使用）:

`adb logcat -v color`
