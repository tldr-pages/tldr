# adb shell

> 在连接的 Android 设备或模拟器上运行 shell 命令。
> 更多信息：<https://developer.android.com/tools/adb>。

- 在模拟器或设备上启动远程交互式 shell：

`adb shell`

- 获取模拟器或设备的所有属性：

`adb shell getprop`

- 将所有运行时权限恢复为默认值：

`adb shell pm reset-permissions`

- 撤销应用程序的危险权限：

`adb shell pm revoke {{package}} {{permission}}`

- 触发一个按键事件：

`adb shell input keyevent {{keycode}}`

- 清除模拟器或设备上应用程序的数据：

`adb shell pm clear {{package}}`

- 在模拟器或设备上启动一个活动：

`adb shell am start -n {{package}}/{{activity}}`

- 在模拟器或设备上启动主屏幕活动：

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`