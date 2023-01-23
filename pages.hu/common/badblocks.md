# badblocks

> Az eszköz rossz blokkok keresése. A badblockok egyes felhasználásai romboló műveleteket okozhatnak, például a lemezen lévő összes adat törlését, beleértve a partíciós táblát is. További információ: <https://manned.org/badblocks>.

- Keressen rossz blokkokat a lemezen egy pusztításmentes, csak olvasható teszt segítségével:

`sudo badblocks {{/dev/sdX}}`

- Egy nem szerelt lemez keresése rossz blokkok után egy roncsolásmentes írási-olvasási teszttel:

`sudo badblocks -n {{/dev/sdX}}`

- A nem szerelt lemez keresése rossz blokkok után destruktív írási teszttel:

`sudo badblocks -w {{/dev/sdX}}`

- Egy nem szerelt lemez keresése rossz blokkok után destruktív írási teszttel és a verbózus állapot megjelenítésével:

`sudo badblocks -svw {{/dev/sdX}}`

- Lekötetlen lemez keresése romboló üzemmódban, és a talált blokkok kimenete egy fájlba:

`sudo badblocks -o {{path/to/file}} -w {{/dev/sdX}}`

- Lekötetlen lemez keresése romboló üzemmódban, nagyobb sebességgel, 4K blokkméret és 64K blokkszám használatával:

`sudo badblocks -w -b {{4096}} -c {{65536}} {{/dev/sdX}}`
