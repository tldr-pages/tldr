# pvs

> A fizikai kötetekre vonatkozó információk megjelenítése. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/pvs.8.html>.

- A fizikai kötetekre vonatkozó információk megjelenítése:

`pvs`

- Nem fizikai kötetek megjelenítése:

`pvs -a`

- Az alapértelmezett megjelenítés módosítása a további részletek megjelenítéséhez:

`pvs -v`

- Csak bizonyos mezők megjelenítése:

`pvs -o {{field_name_1}},{{field_name_2}}`

- Mező hozzáadása az alapértelmezett megjelenítéshez:

`pvs -o +{{field_name}}`

- A címsor elnyomása:

`pvs --noheadings`

- Elválasztójel használata a mezők elválasztására:

`pvs --separator {{special_character}}`
