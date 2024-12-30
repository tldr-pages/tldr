# qdbus

> 最初为Linux开发的进程间通信 (IPC) 和远程过程调用 (RPC) 机制。
> 更多信息：<https://doc.qt.io/qt-5/qtdbus-index.html>。

- 列出可用的服务名称：

`qdbus`

- 列出特定服务的对象路径：

`qdbus {{service_name}}`

- 列出特定对象可用的方法、信号和属性：

`qdbus {{service_name}} {{/path/to/object}}`

- 执行特定方法并传递参数，显示返回值：

`qdbus {{service_name}} {{/path/to/object}} {{method_name}} {{argument1}} {{argument2}}`

- 显示KDE Plasma会话中的当前亮度值：

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness}}`

- 设置KDE Plasma会话中的特定亮度：

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness}} {{5000}}`

- 在KDE Plasma会话中调用音量增加快捷键：

`qdbus {{org.kde.kglobalaccel}} {{/component/kmix}} {{invokeShortcut}} "{{increase_volume}}"`

- 优雅地注销，然后不执行任何操作、重启或关机：

`qdbus {{org.kde.Shutdown}} {{/Shutdown}} {{logout|logoutAndReboot|logoutAndShutdown}}`