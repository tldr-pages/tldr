# x11docker

> Rulați în siguranță aplicații GUI și UI-uri desktop în containere Docker.
> A se vedea, de asemenea, `xephyr`.
> Mai multe informaţii: <https://github.com/mviereck/x11docker>

- Lansarea VLC într-un container:

`x11docker --pulseaudio --share={{$HOME/Videos}} {{jess/vlc}}`

- Lansarea Xfce într-o fereastră:

`x11docker --desktop {{x11docker/xfce}}`

- Lansarea GNOME într-o fereastră:

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/gnome}}`

- Lansează Plasma KDE într-o fereastră:

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/kde-plasma}}`

- Ajutor pentru afișare:

`x11docker --help`
