# plasmashell

> 启动和重启 Plasma 桌面。
> 更多信息：<https://invent.kde.org/plasma/plasma-desktop>。

- 重启 `plasmashell`：

`systemctl restart --user plasma-plasmashell`

- 在不使用 systemd 的情况下重启 `plasmashell`：

`plasmashell --replace & disown`

- 显示命令行选项的 [h]elp：

`plasmashell --help`

- 显示帮助，包括 Qt 选项：

`plasmashell --help-all`