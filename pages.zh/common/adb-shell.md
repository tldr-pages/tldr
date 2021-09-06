# adb shell

> 安卓调试桥-Shell: 运行安卓模拟器或者连接设备上的远程终端命令。
> 更多信息：<https://developer.android.com/studio/command-line/adb>.

- 启动模拟器/设备上的远程终端：

`adb shell`

- 获取模拟器/设备全部属性：

`adb shell getprop`

- 重置所有运行时权限为它们的默认值：

`adb shell pm reset-permissions`

- 撤销一个应用的危险权限：

`adb shell pm revoke {{包名}} {{权限}}`

- 触发一个键盘敲击事件：

`adb shell input keyevent {{键位码}}`

- 清除模拟器/设备上的数据：

`adb shell pm clear {{包名}}`

- 启动模拟器/设备上的一个行为：

`adb shell am start -n {{包名}}/{{活动名}}`

- 启动模拟器/设备上的首页活动：

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
