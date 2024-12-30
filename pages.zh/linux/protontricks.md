# protontricks

> 一个简单的包装器，用于为启用 Proton 的游戏运行 Winetricks 命令。
> 更多信息：<https://github.com/Matoking/protontricks>。

- 运行 protontricks GUI：

`protontricks --gui`

- 为特定游戏运行 Winetricks：

`protontricks {{appid}} {{winetricks_args}}`

- 在游戏安装目录中运行命令：

`protontricks -c {{command}} {{appid}}`

- [l] 列出所有已安装的游戏：

`protontricks -l`

- [s] 按名称搜索游戏的 App ID：

`protontricks -s {{game_name}}`

- 在特定游戏的 proton 环境中运行可执行文件：

`protontricks-launch --appid {{appid}} {{path/to/executable.exe}}`

- 显示帮助：

`protontricks --help`