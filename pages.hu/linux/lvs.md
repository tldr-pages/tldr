# lvs

> A logikai kötetekre vonatkozó információk megjelenítése. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/lvs.8.html>.

- A logikai kötetekre vonatkozó információk megjelenítése:

`lvs`

- Az összes logikai kötet megjelenítése:

`lvs -a`

- Az alapértelmezett megjelenítés módosítása a további részletek megjelenítéséhez:

`lvs -v`

- Csak bizonyos mezők megjelenítése:

`lvs -o {{field_name_1}},{{field_name_2}}`

- Mező hozzáadása az alapértelmezett megjelenítéshez:

`lvs -o +{{field_name}}`

- A címsor elnyomása:

`lvs --noheadings`

- Elválasztójel használata a mezők elválasztásához:

`lvs --separator {{=}}`
