# i3lock

> Az i3 ablakkezelőhöz készült egyszerű képernyőszekrény. További információ: <https://i3wm.org/i3lock>.

- A képernyő zárolása fehér hátteret mutatva:

`i3lock`

- A képernyő zárolása egyszerű színes háttérrel (rrggbb formátumban):

`i3lock --color {{0000ff}}`

- A képernyő zárolása PNG háttérrel:

`i3lock --image {{path/to/file.png}}`

- A képernyő zárolása és a feloldásjelző letiltása (eltávolítja a visszajelzést a billentyű lenyomásakor):

`i3lock --no-unlock-indicator`

- Zárolja a képernyőt, és ne rejtse el az egérmutatót:

`i3lock --pointer {{default}}`

- A képernyő zárolása PNG-háttérrel, amely az összes monitorra kiterjed:

`i3lock --image {{path/to/file.png}} --tiling`

- A képernyő zárolása és a sikertelen bejelentkezési kísérletek számának megjelenítése:

`i3lock --show-failed-attempts`
