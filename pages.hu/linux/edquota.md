# edquota

> Egy felhasználó vagy csoport kvótáinak szerkesztése. Alapértelmezés szerint az összes kvótával rendelkező fájlrendszeren működik. A kvótainformációkat a fájlrendszer gyökerében található `quota.user` és `quota.group` fájlok tárolják állandóan. További információ: <https://manned.org/edquota>.

- Az aktuális felhasználó kvótájának szerkesztése:

`edquota --user $(whoami)`

- Egy adott felhasználó kvótájának szerkesztése:

`sudo edquota --user {{username}}`

- Egy csoport kvótájának szerkesztése:

`sudo edquota --group {{group}}`

- A műveletek korlátozása egy adott fájlrendszerre (alapértelmezés szerint az edquota az összes kvótával rendelkező fájlrendszeren működik):

`sudo edquota --file-system {{filesystem}}`

- Az alapértelmezett türelmi idő szerkesztése:

`sudo edquota -t`

- Kvóta duplikálása más felhasználóknak:

`sudo edquota -p {{reference_user}} {{destination_user1}} {{destination_user2}}`
