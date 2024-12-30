# kreadconfig5

> 读取KDE Plasma的KConfig条目。
> 更多信息：<https://userbase.kde.org/KDE_System_Administration/Configuration_Files>。

- 从全局配置中读取一个键：

`kreadconfig5 --group {{group_name}} --key {{key_name}}`

- 从特定配置文件中读取一个键：

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key_name}}`

- 检查是否使用systemd启动Plasma会话：

`kreadconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}}`