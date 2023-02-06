# scrcpy

> Androidos eszközének megjelenítése és vezérlése asztali számítógépen. További információ: <https://github.com/Genymobile/scrcpy>.

- Egy csatlakoztatott eszköz tükörképének megjelenítése:

`scrcpy`

- Egy adott eszköz tükörképének megjelenítése annak azonosítója vagy IP-címe alapján (a `adb devices` parancs alatt található):

`scrcpy --serial {{0123456789abcdef|192.168.0.1:5555}}`

- Megjelenítés indítása teljes képernyős módban:

`scrcpy --fullscreen`

- A kijelző képernyő elforgatása. Minden növekményes érték egy 90 fokos elforgatást ad az óramutató járásával ellentétes irányban:

`scrcpy --rotation {{0|1|2|3}}`

- A fizikai eszköz érintéseinek megjelenítése:

`scrcpy --show-touches`

- A kijelző képernyő rögzítése:

`scrcpy --record {{path/to/file.mp4}}`

- Célkönyvtár beállítása a fájlok eszközre húzással történő áthelyezéséhez (nem APK):

`scrcpy --push-target {{path/to/directory}}`
