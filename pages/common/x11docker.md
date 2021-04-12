# x11docker

> Run GUI applications and desktops in docker giving focus on security.
> See also `xephyr`.
> More information: <https://github.com/mviereck/x11docker>.

- Launch VLC in a container:

`x11docker --pulseaudio --share={{$HOME/Videos}} {{jess/vlc}}`

- Launch Xfce in a window:

`x11docker --desktop {{x11docker/lxde}}`

- Launch GNOME in a window:

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/gnome}}`

- Launch KDE Plasma in a window:

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/kde-plasma}}`

- Display help:

`x11docker --help`
