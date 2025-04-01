# qjoypad

> 将游戏手柄或摇杆的输入转换为键盘按键或鼠标动作。
> 更多信息：<https://qjoypad.sourceforge.net/>。

- 启动 QJoyPad：

`qjoypad`

- 指定目录启动 QJoyPad 并搜索设备：

`qjoypad --device={{path/to/directory}}`

- 启动 QJoyPad 但不显示系统托盘图标：

`qjoypad --notray`

- 启动 QJoyPad 并强制窗口管理器使用系统托盘图标：

`qjoypad --force-tray`

- 强制正在运行的 QJoyPad 实例更新其设备和布局列表：

`qjoypad --update`

- 在已经运行的 QJoyPad 实例中加载指定布局，或使用指定布局启动 QJoyPad：

`qjoypad "{{layout}}"`
