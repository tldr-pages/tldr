# xattr

> Segédprogram a kiterjesztett fájlrendszer-attribútumokkal való munkához. További információ: <https://ss64.com/osx/xattr.html>.

- Kulcs:érték kiterjesztett attribútumok listája egy adott fájlhoz:

`xattr -l {{file}}`

- Adott fájl attribútumának kiírása:

`xattr -w {{attribute_key}} {{attribute_value}} {{file}}`

- Attribútum törlése egy adott fájlból:

`xattr -d {{com.apple.quarantine}} {{file}}`

- Az összes kiterjesztett attribútum törlése egy adott fájlból:

`xattr -c {{file}}`

- Attribútum rekurzív törlése egy adott könyvtárban:

`xattr -rd {{attribute_key}} {{directory}}`
