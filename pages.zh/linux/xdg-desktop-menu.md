# xdg-desktop-menu

> 用于安装或卸载桌面菜单项的命令行工具。
> 更多信息：<https://manned.org/xdg-desktop-menu>.

- 将应用程序安装到桌面菜单系统：

`xdg-desktop-menu install {{path/to/file.desktop}}`

- 安装应用程序到桌面菜单系统时禁用供应商前缀检查：

`xdg-desktop-menu install --novendor {{path/to/file.desktop}}`

- 从桌面菜单系统卸载应用程序：

`xdg-desktop-menu uninstall {{path/to/file.desktop}}`

- 强制更新桌面菜单系统：

`xdg-desktop-menu forceupdate --mode {{user|system}}`
