# vgs

> A kötetcsoportokra vonatkozó információk megjelenítése. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/vgs.8.html>.

- A kötetcsoportokra vonatkozó információk megjelenítése:

`vgs`

- Az összes kötetcsoport megjelenítése:

`vgs -a`

- Az alapértelmezett megjelenítés módosítása a további részletek megjelenítéséhez:

`vgs -v`

- Csak bizonyos mezők megjelenítése:

`vgs -o {{field_name_1}},{{field_name_2}}`

- Mező hozzáadása az alapértelmezett megjelenítéshez:

`vgs -o +{{field_name}}`

- A címsor elnyomása:

`vgs --noheadings`

- Elválasztójel használata a mezők elválasztására:

`vgs --separator =`
