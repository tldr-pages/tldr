# screenkey

> A képernyőbe nyomtatott billentyűk megjelenítésére szolgáló eszköz. További információ: <https://www.thregr.org/~wavexx/software/screenkey/>.

- Az éppen lenyomott billentyűk megjelenítése a képernyőn:

`screenkey`

- Az éppen lenyomott billentyűk és egérgombok megjelenítése a képernyőn:

`screenkey --mouse`

- A screenkey beállítási menüjének elindítása:

`screenkey --show-settings`

- A képernyőbillentyű egy adott pozícióban történő elindítása:

`screenkey --position {{top|center|bottom|fixed}}`

- A képernyőn megjelenített billentyűmódosítók formátumának módosítása:

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- A képernyőbillentyű megjelenésének módosítása:

`screenkey --bg-color "{{#a1b2c3}}" --font {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- Húzza és válassza ki a képernyőn az ablakot a képernyőbillentyű megjelenítéséhez:

`screenkey --position fixed --geometry {{$(slop -n -f '%g')}}`
