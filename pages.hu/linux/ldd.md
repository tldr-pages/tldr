# ldd

> Megjeleníti egy bináris program megosztott könyvtárfüggőségeit. Ne használja nem megbízható bináris programmal, használja helyette az objdump-ot. További információ: <https://manned.org/ldd>.

- Egy bináris program megosztott könyvtárfüggőségének megjelenítése:

`ldd {{path/to/binary}}`

- A függőségekre vonatkozó összes információ megjelenítése:

`ldd --verbose {{path/to/binary}}`

- Nem használt közvetlen függőségek megjelenítése:

`ldd --unused {{path/to/binary}}`

- Hiányzó adatobjektumok jelentése és adatáthelyezések végrehajtása:

`ldd --data-relocs {{path/to/binary}}`

- Hiányzó adatobjektumok és függvények jelentése, és mindkettő esetében áthelyezések végrehajtása:

`ldd --function-relocs {{path/to/binary}}`
