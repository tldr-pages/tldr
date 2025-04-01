# kwriteconfig5

> 为 KDE Plasma 写入 KConfig 条目。
> 更多信息：<https://userbase.kde.org/KDE_System_Administration/Configuration_Files>。

- 显示帮助：

`kwriteconfig5 --help`

- 设置全局配置键：

`kwriteconfig5 --group {{group_name}} --key {{key}} {{value}}`

- 在特定配置文件中设置键：

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key}} {{value}}`

- 删除键：

`kwriteconfig5 --group {{group_name}} --key {{key}} --delete`

- 当可用时使用 systemd 启动 Plasma 会话：

`kwriteconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}} {{true}}`

- 当窗口最大化时隐藏标题栏（类似 Ubuntu）：

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{Windows}} --key {{BorderlessMaximizedWindows}} {{true}}`

- 配置 KRunner 以 Meta（命令/Windows）全局热键打开：

`kwriteconfig5 --file {{~/.config/kwinrc}} --group {{ModifierOnlyShortcuts}} --key {{Meta}} "{{org.kde.kglobalaccel,/component/krunner_desktop,org.kde.kglobalaccel.Component,invokeShortcut,_launch}}"`
