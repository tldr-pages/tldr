# qdbus

> 进程间通信 (IPC) 和远程过程调用 (RPC) 机制，最初在 Linux 上开发。
> 更多信息：<https://doc.qt.io/qt-5/qtdbus-index.html>.

- 列出可用的服务名称：

`qdbus`

- 列出指定服务的对象路径：

`qdbus {{服务名}}`

- 列出指定对象可用的方法、信号和属性：

`qdbus {{服务名}} {{路径/到/对象}}`

- 执行指定方法，传递参数并显示返回值：

`qdbus {{服务名}} {{路径/到/对象}} {{方法名}} {{参数1}} {{参数2}}`

- 显示在 KDE Plasma 会话中的当前亮度值：

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness}}`

- 设置 KDE Plasma 会话中的特定亮度：

`qdbus {{org.kde.Solid.PowerManagement}} {{/org/kde/Solid/PowerManagement/Actions/BrightnessControl}} {{org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness}} {{5000}}`

- 在 KDE Plasma 会话中调用音量增大快捷键：

`qdbus {{org.kde.kglobalaccel}} {{/component/kmix}} {{invokeShortcut}} "{{increase_volume}}"`

- 优雅地注销并然后选择不执行任何操作、重启或关机：

`qdbus {{org.kde.Shutdown}} {{/Shutdown}} {{logout|logoutAndReboot|logoutAndShutdown}}`
