# dm-tool

> A kijelzőkezelővel való kommunikáció eszköze. További információ: <https://manned.org/dm-tool>.

- Az üdvözlő megjelenítése, miközben az aktuális asztali munkamenet nyitva marad, és arra vár, hogy a bejelentkezett felhasználó hitelesítését követően visszaállítsa:

`dm-tool switch-to-greeter`

- Az aktuális munkamenet zárolása:

`dm-tool lock`

- Átváltás egy adott felhasználóra, szükség esetén hitelesítési kérés megjelenítése:

`dm-tool switch-to-user {{username}} {{session}}`

- Dinamikus ülés hozzáadása egy futó LightDM-munkamenetből:

`dm-tool add-seat {{xlocal}} {{name}}={{value}}`
