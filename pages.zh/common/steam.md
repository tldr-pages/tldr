# Steam

> Valve开发的视频游戏平台。
> 更多信息：<https://developer.valvesoftware.com/wiki/Command_Line_Options>。

- 启动Steam，并将调试消息打印到`stdout`：

`steam`

- 启动Steam并启用其应用内调试控制台选项卡：

`steam -console`

- 在正在运行的Steam实例中启用并打开Steam控制台选项卡：

`steam steam://open/console`

- 使用指定的凭据登录Steam：

`steam -login {{username}} {{password}}`

- 以大屏幕模式启动Steam：

`steam -tenfoot`

- 退出Steam：

`steam -shutdown`