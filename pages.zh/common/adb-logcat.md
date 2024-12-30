# adb logcat

> 转储系统消息的日志。
> 更多信息：<https://developer.android.com/tools/logcat>。

- 显示系统日志：

`adb logcat`

- 显示匹配正则表达式的行：

`adb logcat -e {{正则表达式}}`

- 以特定模式（[V]详细，[D]调试，[I]信息，[W]警告，[E]错误，[F]致命，[S]静默）显示特定标签的日志，过滤其他标签：

`adb logcat {{标签}}:{{模式}} *:S`

- 以详细模式显示 React Native 应用程序的日志，静默其他标签：

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- 显示所有标签的日志，优先级为警告及以上：

`adb logcat *:W`

- 显示特定 PID 的日志：

`adb logcat --pid {{pid}}`

- 显示特定包的进程日志：

`adb logcat --pid $(adb shell pidof -s {{包名}})`

- 为日志上色（通常与过滤器一起使用）：

`adb logcat -v color`