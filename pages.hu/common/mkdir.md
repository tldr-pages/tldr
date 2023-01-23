# mkdir

> Könyvtárak létrehozása és jogosultságaik beállítása. További információ: <https://www.gnu.org/software/coreutils/mkdir>.

- Speciális könyvtárak létrehozása:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- Hozzon létre konkrét könyvtárakat és szükség esetén \[p\]arentjeiket:

`mkdir -p {{path/to/directory1 path/to/directory2 ...}}`

- Hozzon létre könyvtárakat meghatározott engedélyekkel:

`mkdir -m {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`
