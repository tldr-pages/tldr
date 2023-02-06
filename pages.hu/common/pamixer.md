# pamixer

> Egy egyszerű parancssori keverő a PulseAudio-hoz. További információ: <https://github.com/cdemoulins/pamixer>.

- Listázza az összes elnyelőt és forrást a megfelelő azonosítókkal:

`pamixer --list-sinks --list-sources`

- Állítsa a hangerőt 75%-ra az alapértelmezett nyelőn:

`pamixer --set-volume {{75}}`

- A némítás bekapcsolása az alapértelmezettől eltérő nyelőn:

`pamixer --toggle-mute --sink {{ID}}`

- Növelje a hangerőt az alapértelmezett nyelőn 5%-kal:

`pamixer --increase {{5}}`

- Csökkentse a hangerőt egy forráson 5%-kal:

`pamixer --decrease {{5}} --source {{ID}}`

- A hangerő növelésének, csökkentésének vagy 100% feletti hangerő beállításának engedélyezése a boost opcióval:

`pamixer --set-volume {{105}} --allow-boost`

- Az alapértelmezett nyelő némítása (a némítás feloldásához használja a `--unmute` helyett):

`pamixer --mute`
