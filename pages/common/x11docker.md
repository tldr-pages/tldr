# x11docker

> Securely run GUI applications and desktop UIs in Docker containers.
> See also: `xephyr`.
> More information: <https://github.com/mviereck/x11docker#terminal-syntax>.

- Launch VLC in a container:

`x11docker {{[-p|--pulseaudio]}} --share {{$HOME/Videos}} {{jess/vlc}}`

- Launch Xfce in a window:

`x11docker {{[-d|--desktop]}} {{x11docker/xfce}}`

- Launch GNOME in a window:

`x11docker {{[-d|--desktop]}} {{[-g|--gpu]}} --init={{systemd}} {{x11docker/gnome}}`

- Launch KDE Plasma in a window:

`x11docker {{[-d|--desktop]}} {{[-g|--gpu]}} --init={{systemd}} {{x11docker/kde-plasma}}`

- Display help:

`x11docker --help`
