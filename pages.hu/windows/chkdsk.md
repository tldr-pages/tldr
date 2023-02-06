# chkdsk

> A fájlrendszer és a kötet metaadatainak hibaellenőrzése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- Adja meg az ellenőrizni kívánt meghajtó betűjelét (kettőspont után), csatolási pontot vagy kötetnevet:

`chkdsk {{volume}}`

- Egy adott kötet hibáinak javítása:

`chkdsk {{volume}} /f`

- Egy adott kötet leválasztása az ellenőrzés előtt:

`chkdsk {{volume}} /x`

- A naplófájl méretének módosítása a megadott méretre (csak NTFS esetén):

`chkdsk /l{{size}}`
