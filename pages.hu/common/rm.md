# rm

> Fájlok vagy könyvtárak eltávolítása. Lásd még: `rmdir`. További információ: <https://www.gnu.org/software/coreutils/rm>.

- Bizonyos fájlok eltávolítása:

`rm {{path/to/file1 path/to/file2 ...}}`

- Bizonyos fájlok eltávolítása, figyelmen kívül hagyva a nem létező fájlokat:

`rm -f {{path/to/file1 path/to/file2 ...}}`

- Bizonyos fájlok eltávolítása \[i\]nteraktívan, minden egyes eltávolítás előtt kérdezve:

`rm -i {{path/to/file1 path/to/file2 ...}}`

- Bizonyos fájlok eltávolítása: minden egyes eltávolításról szóló információ nyomtatása:

`rm -v {{path/to/file1 path/to/file2 ...}}`

- Bizonyos fájlok és könyvtárak eltávolítása \[r\]ekurzívan:

`rm -r {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
