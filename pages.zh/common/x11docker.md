# x11docker

> 在 Docker 容器中安全运行图形应用程序和桌面界面。
> 另见 `xephyr`。
> 更多信息：<https://github.com/mviereck/x11docker>。

- 在容器中启动 VLC：

`x11docker --pulseaudio --share={{$HOME/Videos}} {{jess/vlc}}`

- 在窗口中启动 Xfce：

`x11docker --desktop {{x11docker/xfce}}`

- 在窗口中启动 GNOME：

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/gnome}}`

- 在窗口中启动 KDE Plasma：

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/kde-plasma}}`

- 显示帮助：

`x11docker --help`
