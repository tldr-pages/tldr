# winetricks

> 管理 Wine 虚拟 Windows 环境。
> 更多信息：<https://wiki.winehq.org/Winetricks>.

- 在默认的 Wine 位置启动图形化设置：

`winetricks`

- 指定自定义的 Wine 目录以运行 Winetricks：

`WINEPREFIX={{path/to/wine_directory}} winetricks`

- 在默认的 Wine 目录中安装 Windows DLL 或组件：

`winetricks {{package}}`