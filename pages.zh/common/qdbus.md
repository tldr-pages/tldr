# qdbus

> 进程间通信（IPC）和远程过程调用（RPC）机制，最初为 Linux 研发。
> 更多信息：<https://doc.qt.io/qt-5/qtdbus-index.html>.

- 列出可用的服务名称：

`qdbus`

- 列出特定服务的对象路径：

`qdbus {{service_name}}`

- 列出特定对象上可用的方法、信号和属性：

`qdbus {{service_name}} {{/path/to/object}}`

- 传递参数执行特定方法并显示返回值：

`qdbus {{service_name}} {{/path/to/object}} {{method_name}} {{argument1}} {{argument2}}`

- 显示 KDE Plasma 会话中的当前亮度值：

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness}}`

- 在 KDE Plasma 会话中设置特定的亮度：

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness}} {{5000}}`

- 在 KDE Plasma 会话中调用音量增加快捷键：

`qdbus {{org.kde.kglobalaccel}} {{/component/kmix}} {{invokeShortcut}} "{{increase_volume}}"`

- 正常注销，然后不做任何操作、重启或关闭计算机：

`qdbus {{org.kde.Shutdown}} {{/Shutdown}} {{logout|logoutAndReboot|logoutAndShutdown}}`
