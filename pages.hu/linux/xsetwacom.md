# xsetwacom

> Parancssori eszköz a Wacom tolltáblák beállításainak futás közbeni módosítására. További információ: <https://manned.org/xsetwacom>.

- Az összes elérhető Wacom eszköz listája. Az eszköz neve az első oszlopban található:

`xsetwacom list`

- Wacom terület beállítása egy adott képernyőre. A képernyő nevének lekérdezése a `xrandr` címmel:

`xsetwacom set "{{device_name}}" MapToOutput {{screen}}`

- Állítsa be a módot relatív (mint az egér) vagy abszolút (mint a toll) módra:

`xsetwacom set "{{device_name}}" Mode "{{Relative|Absolute}}"`

- A bemenet elforgatása (hasznos tablet-PC esetén a képernyő elforgatásakor) 0|90|180|270 fokkal a "természetes" elforgatástól:

`xsetwacom set "{{device_name}}" Rotate {{none|half|cw|ccw}}`

- Állítsa be, hogy a gomb csak akkor működjön, ha a toll hegye a táblagéphez ér:

`xsetwacom set "{{device_name}}" TabletPCButton "on"`
