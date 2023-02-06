# cipher

> NTFS köteteken lévő könyvtárak és fájlok titkosításának megjelenítése vagy módosítása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- Egy adott titkosított fájlra vagy könyvtárra vonatkozó információk megjelenítése:

`cipher /c:{{path/to/file_or_directory}}`

- \[e\]ncrypt a file or directory (a könyvtárhoz később hozzáadott fájlok is titkosítva lesznek, ahogy a könyvtárat megjelöli):

`cipher /e:{{path/to/file_or_directory}}`

- \[d\]ecrypt a file or directory:

`cipher /d:{{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár biztonságos eltávolítása:

`cipher /w:{{path/to/file_or_directory}}`
