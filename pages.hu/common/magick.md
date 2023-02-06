# magick

> Bittérképes képek létrehozása, szerkesztése, összeállítása vagy konvertálása. 7+ verziójú ImageMagick. A 6-os és az alatti verziókhoz lásd: `convert`. További információ: <https://imagemagick.org/>.

- Fájltípus átalakítása:

`magick {{image.png}} {{image.jpg}}`

- Kép átméretezése, új másolat készítése:

`magick convert -resize {{100x100}} {{image.jpg}} {{image.jpg}}`

- GIF létrehozása képek felhasználásával:

`magick {{*.jpg}} {{images.gif}}`

- Sakk-mintázat létrehozása:

`magick -size {{640x480}} pattern:checkerboard {{checkerboard.png}}`

- Képek konvertálása egyedi PDF-oldalakká:

`magick {{*.jpg}} +adjoin {{page-%d.pdf}}`
