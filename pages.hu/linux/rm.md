# rm

> Fájlok vagy könyvtárak eltávolítása. Lásd még: `rmdir`. További információ: <https://www.gnu.org/software/coreutils/rm>.

- Bizonyos fájlok eltávolítása:

`rm {{path/to/file1 path/to/file2 ...}}`

- Bizonyos fájlok eltávolítása, figyelmen kívül hagyva a nem létező fájlokat:

`rm --force {{path/to/file1 path/to/file2 ...}}`

- Bizonyos fájlok eltávolítása interaktívan, minden egyes eltávolítás előtt kérdezősködve:

`rm --interactive {{path/to/file1 path/to/file2 ...}}`

- Bizonyos fájlok eltávolítása: minden egyes eltávolításról szóló információ kinyomtatása:

`rm --verbose {{path/to/file1 path/to/file2 ...}}`

- Bizonyos fájlok és könyvtárak rekurzív eltávolítása:

`rm --recursive {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
