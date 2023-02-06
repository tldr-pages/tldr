# enca

> Szövegfájlok kódolásának felismerése és átalakítása. További információ: <https://github.com/nijel/enca>.

- A fájl(ok) kódolásának felismerése a rendszer területi beállításainak megfelelően:

`enca {{path/to/file1 path/to/file2 ...}}`

- A POSIX/C locale formátumú (pl. zh_CN, en_US) nyelvi kódolású fájl(ok) felismerése:

`enca -L {{language}} {{path/to/file1 path/to/file2 ...}}`

- A fájl(ok) átalakítása egy adott kódolásra:

`enca -L {{language}} -x {{to_encoding}} {{path/to/file1 path/to/file2 ...}}`

- Egy meglévő fájl másolatának létrehozása más kódolással:

`enca -L {{language}} -x {{to_encoding}} < {{original_file}} > {{new_file}}`
