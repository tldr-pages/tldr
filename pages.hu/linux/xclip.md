# xclip

> X11 vágólap manipulációs eszköz, hasonlóan a `xsel`-hoz. Kezeli az X elsődleges és másodlagos kiválasztásokat, valamint a rendszer vágólapját (`Ctrl + C`/`Ctrl + V`). További információ: <https://manned.org/xclip>.

- Egy parancs kimenetének másolása az X11 elsődleges kiválasztási területére (vágólap):

`echo 123 | xclip`

- Egy parancs kimenetének másolása egy adott X11 kijelölési területre:

`echo 123 | xclip -selection {{primary|secondary|clipboard}}`

- Egy parancs kimenetének másolása a rendszer vágólapjára, rövid jelöléssel:

`echo 123 | xclip -sel clip`

- Egy fájl tartalmának másolása a rendszer vágólapjára:

`xclip -sel clip {{input_file.txt}}`

- Egy PNG tartalmának másolása a rendszer vágólapjára (más programokban helyesen beilleszthető):

`xclip -sel clip -t image/png {{input_file.png}}`

- A konzolon lévő felhasználói bemenet másolása a rendszer vágólapjára:

`xclip -i`

- Az X11 elsődleges kiválasztási terület tartalmának beillesztése a konzolba:

`xclip -o`

- A rendszer vágólapjának tartalmának beillesztése a konzolba:

`xclip -o -sel clip`
