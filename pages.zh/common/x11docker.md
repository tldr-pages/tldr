# x11docker

> 在Docker容器中安全地运行GUI应用程序和桌面用户界面。
> 另见 `xephyr`。
> 更多信息请访问：<https://github.com/mviereck/x11docker>。

- 在容器中启动VLC：

`x11docker --pulseaudio --share={{$HOME/Videos}} {{jess/vlc}}`

- 在窗口中启动Xfce：

`x11docker --desktop {{x11docker/xfce}}`

- 在窗口中启动GNOME：

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/gnome}}`

- 在窗口中启动KDE Plasma：

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/kde-plasma}}`

- 显示帮助信息：

`x11docker --help`