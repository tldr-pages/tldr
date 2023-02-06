# repquota

> A fájlrendszer meglévő fájlkvótáinak összefoglalójának megjelenítése. További információ: <https://manned.org/repquota>.

- Az összes használt kvóta statisztikáinak jelentése:

`sudo repquota -all`

- A kvóta statisztikák jelentése minden felhasználó számára, még azok számára is, akik nem használják a kvótájukat:

`sudo repquota -v {{filesystem}}`

- Csak a felhasználók kvótáiról szóló jelentés:

`repquota --user {{filesystem}}`

- Csak a csoportok kvótáiról szóló jelentés:

`sudo repquota --group {{filesystem}}`

- Jelentés a felhasznált kvótákról és korlátokról ember által olvasható formátumban:

`sudo repquota --human-readable {{filesystem}}`

- Jelentés a felhasználók és csoportok összes kvótájáról ember által olvasható formátumban:

`sudo repquota -augs`
