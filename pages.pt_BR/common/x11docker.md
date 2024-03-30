# x11docker

> Executar aplicativos de GUI e interfaces de desktop seguramente em contêineres do Docker.
> Veja também `xephyr`.
> Mais informações: <https://github.com/mviereck/x11docker>.

- Inicia o VLC em um contêiner:

`x11docker --pulseaudio --share={{$HOME/Videos}} {{jess/vlc}}`

- Inicia o Xfce em uma janela:

`x11docker --desktop {{x11docker/xfce}}`

- Inicia o GNOME em uma janela:

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/gnome}}`

- Inicia o KDE Plasma em uma janela:

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/kde-plasma}}`

- Exibe ajuda:

`x11docker --help`
