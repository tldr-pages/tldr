# montage

> ImageMagick képmontázs eszköz. Képeket helyez el egy testreszabható rácsba. További információ: <https://imagemagick.org/script/montage.php>.

- Képek rácsba rakása, a rács cellaméreténél nagyobb képek automatikus átméretezése:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} montage.jpg`

- Képek rácsba rakása, a rácscellák méretének automatikus kiszámítása a legnagyobb képből:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 montage.jpg`

- Állítsa be a rácscellaméretet, és a képeket a rácsra helyezés előtt méretezze át, hogy illeszkedjenek hozzá:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry 640x480+0+0 montage.jpg`

- Korlátozza a sorok és oszlopok számát a rácsban, a bemeneti képek több kimeneti montázsba való túlcsordulását okozva:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 -tile 2x3 montage_%d.jpg`

- A képek méretének módosítása és kivágása, hogy kitöltsék a rácscellákat a csempézés előtt:

`montage {{image1.png}} {{image2.jpg}} {{imageN.png}} -geometry +0+0 -resize 640x480^ -gravity center -crop 640x480+0+0 montage.jpg`
