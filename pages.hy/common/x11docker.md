# x11docker

> Ապահով գործարկեք GUI հավելվածները և աշխատասեղանի միջերեսները Docker կոնտեյներներում:.
> Տես նաև՝ `xephyr`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mviereck/x11docker#terminal-syntax>:.

- Գործարկել VLC-ն կոնտեյներով.:

`x11docker {{[-p|--pulseaudio]}} --share {{$HOME/Videos}} {{jess/vlc}}`

- Գործարկեք Xfce-ը պատուհանում.:

`x11docker {{[-d|--desktop]}} {{x11docker/xfce}}`

- Գործարկել GNOME-ը պատուհանում.:

`x11docker {{[-d|--desktop]}} {{[-g|--gpu]}} --init={{systemd}} {{x11docker/gnome}}`

- Գործարկել KDE Plasma-ն պատուհանում.:

`x11docker {{[-d|--desktop]}} {{[-g|--gpu]}} --init={{systemd}} {{x11docker/kde-plasma}}`

- Ցուցադրել օգնությունը.:

`x11docker --help`
