# kde-inhibit

> Különböző asztali funkciók letiltása egy parancs futása közben. További információ: <https://invent.kde.org/plasma/kde-cli-tools/-/blob/master/kdeinhibit/main.cpp>.

- Az energiagazdálkodás letiltása:

`kde-inhibit --power {{command}} {{command_arguments}}`

- Képernyőkímélő letiltása:

`kde-inhibit --screenSaver {{command}} {{command_arguments}}`

- A VLC elindítása, és a színkorrekció (éjszakai üzemmód) gátlása, amíg az fut:

`kde-inhibit --colorCorrect {{vlc}}`
