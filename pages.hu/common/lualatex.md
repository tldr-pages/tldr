# lualatex

> A TeX kiterjesztett változata, amely a Lua-t használja a fordításhoz. További információ: <https://manned.org/lualatex.1>.

- Indítsa el a `texlua` oldalt, hogy Lua-értelmezőként működjön:

`lualatex`

- Egy Tex-fájl PDF-be fordítása:

`lualatex {{path/to/file.tex}}`

- Tex fájl fordítása hiba megszakítás nélkül:

`lualatex -interaction nonstopmode {{path/to/file.tex}}`

- Tex fájl fordítása egy adott kimeneti fájlnévvel:

`lualatex -jobname={{filename}} {{path/to/file.tex}}`
