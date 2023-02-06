# fc

> Két fájl vagy fájlkészlet közötti különbségek összehasonlítása. A fájlkészletek összehasonlításához használjon helyettesítő karaktereket (\*). További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/fc>.

- 2 megadott fájl összehasonlítása:

`fc {{path/to/file_1}} {{path/to/file_2}}`

- Nagy- és kisbetűket nem figyelembe vevő összehasonlítás elvégzése:

`fc /c {{path/to/file_1}} {{path/to/file_2}}`

- Fájlok összehasonlítása Unicode szövegként:

`fc /u {{path/to/file_1}} {{path/to/file_2}}`

- Fájlok összehasonlítása ASCII szövegként:

`fc /l {{path/to/file_1}} {{path/to/file_2}}`

- Fájlok összehasonlítása bináris formában:

`fc /b {{path/to/file_1}} {{path/to/file_2}}`

- A tabulátorok szóközökre való kiterjesztésének kikapcsolása:

`fc /t {{path/to/file_1}} {{path/to/file_2}}`

- A szóközök (tabulátorok és szóközök) tömörítése az összehasonlításokhoz:

`fc /w {{path/to/file_1}} {{path/to/file_2}}`
