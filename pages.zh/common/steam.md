# steam

> Valve 的电子游戏平台。
> 更多信息：<https://developer.valvesoftware.com/wiki/Command_Line_Options>.

- 启动 Steam 同时将调试信息输出到 `stdout`:

`steam`

- 启动 Steam 并启用内置调试控制台标签页：

`steam -console`

- 在运行的 Steam 实例中启用并打开控制台标签页：

`steam steam://open/console`

- 使用指定认证信息登录 Steam:

`steam -login {{username}} {{password}}`

- 以大屏幕模式启动 Steam:

`steam -tenfoot`

- 退出 Steam:

`steam -shutdown`
