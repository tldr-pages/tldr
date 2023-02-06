# kitty

> Gyors, funkciógazdag, GPU-alapú terminál emulátor. További információ: <https://sw.kovidgoyal.net/kitty/>.

- Nyisson egy új terminált:

`kitty`

- Terminál megnyitása az ablak megadott címével:

`kitty --title "{{title}}"`

- Indítsa el a beépített témaválasztót:

`kitty +kitten themes`

- Kép megjelenítése a terminálban:

`kitty +kitten icat {{path/to/image}}`

- A `stdin` tartalmának másolása a vágólapra:

`echo {{example}} | kitty +kitten clipboard`
