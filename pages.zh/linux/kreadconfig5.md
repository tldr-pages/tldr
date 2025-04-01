# kreadconfig5

> 读取 KDE Plasma 的 KConfig 条目。
> 更多信息：<https://userbase.kde.org/KDE_System_Administration/Configuration_Files>。

- 从全局配置中读取一个键：

`kreadconfig5 --group {{group_name}} --key {{key_name}}`

- 从特定配置文件中读取一个键：

`kwriteconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key_name}}`

- 检查是否使用 systemd 启动 Plasma 会话：

`kreadconfig5 --file {{startkderc}} --group {{General}} --key {{systemdBoot}}`
