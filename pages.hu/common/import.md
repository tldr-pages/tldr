# import

> Az X-kiszolgáló képernyőjének egy részének vagy egészének rögzítése, és a kép mentése egy fájlba. Az ImageMagick könyvtár része. További információ: <https://imagemagick.org/script/import.php>.

- A teljes X-kiszolgáló képernyőjének rögzítése PostScript képformátumban:

`import -window root {{output.postscript}}`

- Egy távoli X-kiszolgáló képernyő tartalmának rögzítése PNG formátumban:

`import -window root -display {{remote_host}}:{{screen}}.{{display}} {{output.png}}`

- Egy adott ablak rögzítése JPEG formátumban, a `xwininfo` által megjelenített azonosítójával:

`import -window {{window_id}} {{output.jpg}}`
