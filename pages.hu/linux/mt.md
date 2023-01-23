# mt

> A mágnesszalag-meghajtó működésének vezérlése (általában LTO-szalag). További információ: <https://manned.org/mt>.

- A szalagmeghajtó állapotának ellenőrzése:

`mt -f {{/dev/nstX}} status`

- A szalag visszatekerése a kezdethez:

`mt -f {{/dev/nstX}} rewind`

- Előre mozgatni egy adott fájlt, majd a szalagot a következő fájl első blokkjára pozícionálni:

`mt -f {{/dev/nstX}} fsf {{count}}`

- A szalag visszatekerése, majd a szalag pozícionálása az adott fájl elejére:

`mt -f {{/dev/nstX}} asf {{count}}`

- A szalag pozicionálása az érvényes adat végére:

`mt -f {{/dev/nstX}} eod`

- Tekerje vissza a szalagot, és vegye ki/ki a szalagot:

`mt -f {{/dev/nstX}} eject`

- EOF (fájl vége) jel írása az aktuális pozícióra:

`mt -f {{/dev/nstX} eof`
