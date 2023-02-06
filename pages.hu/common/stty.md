# stty

> Beállítások beállítása egy termináleszköz interfészéhez. További információ: <https://www.gnu.org/software/coreutils/stty>.

- Az aktuális terminál összes beállításának megjelenítése:

`stty --all`

- A sorok vagy oszlopok számának beállítása:

`stty {{rows|cols}} {{count}}`

- Az eszköz tényleges átviteli sebességének lekérdezése:

`stty --file {{path/to/device_file}} speed`

- Az összes üzemmód visszaállítása az aktuális terminál számára ésszerű értékekre:

`stty sane`
