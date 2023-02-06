# jtbl

> Segédprogram JSON és JSON Lines adatok táblázatos formában történő kinyomtatásához a terminálban. További információ: <https://github.com/kellyjonbrazil/jtbl>.

- Táblázat nyomtatása JSON vagy JSON Lines bemenetből:

`cat {{file.json}} | jtbl`

- Táblázat nyomtatása és az oszlopszélesség megadása a felgöngyölítéshez:

`cat {{file.json}} | jtbl --cols={{width}}`

- Táblázat nyomtatása és a sorok csonkítása a csomagolás helyett:

`cat {{file.json}} | jtbl -t`

- Táblázat nyomtatása, és a sorok nem csomagolása vagy csonkítása:

`cat {{file.json}} | jtbl -n`
