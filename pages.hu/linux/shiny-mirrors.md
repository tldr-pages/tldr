# shiny-mirrors

> A pacman tükörlista generálása a Manjaro Linuxhoz. A shiny-mirrors minden futtatásakor szinkronizálni kell az adatbázist és frissíteni a rendszert a `sudo pacman -Syyu` segítségével. További információ: <https://gitlab.com/Arisa_Snowbell/shiny-mirrors/-/blob/domina/shiny-mirrors/man/shiny-mirrors.md>.

- Az aktuális tükrök állapotának lekérdezése:

`shiny-mirrors status`

- Tükörlista generálása az alapértelmezett viselkedés szerint:

`sudo shiny-mirrors refresh`

- Az aktuális konfigurációs fájl megjelenítése:

`shiny-mirrors config show`

- Váltson át interaktívan egy másik ágra:

`sudo shiny-mirrors config --branch`
