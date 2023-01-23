# xbacklight

> Segédprogram a háttérvilágítás fényerejének beállításához a RandR kiterjesztés segítségével. További információ: <https://gitlab.freedesktop.org/xorg/app/xbacklight>.

- A képernyő aktuális fényerejének lekérdezése százalékos formában:

`xbacklight`

- A képernyő fényerejét 40%-ra állítja:

`xbacklight -set {{40}}`

- Növelje az aktuális fényerőt 25%-kal:

`xbacklight -inc {{25}}`

- Csökkentse az aktuális fényerőt 75%-kal:

`xbacklight -dec {{75}}`

- Növelje a háttérvilágítást 100%-ra, 60 másodperc alatt (az érték ms-ban van megadva), 60 lépésben:

`xbacklight -set {{100}} -time {{60000}} -steps {{60}}`
