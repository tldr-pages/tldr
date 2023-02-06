# x11docker

> GUI-alkalmazások és asztali felhasználói felületek biztonságos futtatása Docker-konténerekben. Lásd még: `xephyr`. További információ: <https://github.com/mviereck/x11docker>.

- A VLC elindítása konténerben:

`x11docker --pulseaudio --share={{$HOME/Videos}} {{jess/vlc}}`

- Az Xfce elindítása egy ablakban:

`x11docker --desktop {{x11docker/xfce}}`

- A GNOME elindítása egy ablakban:

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/gnome}}`

- KDE Plasma indítása egy ablakban:

`x11docker --desktop --gpu --init={{systemd}} {{x11docker/kde-plasma}}`

- Súgó megjelenítése:

`x11docker --help`
