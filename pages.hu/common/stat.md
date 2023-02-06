# stat

> Fájl- és fájlrendszerinformációk megjelenítése. További információ: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Egy adott fájl tulajdonságainak megjelenítése, mint például a méret, az engedélyek, a létrehozás és a hozzáférés dátuma, többek között:

`stat {{path/to/file}}`

- Egy adott fájl tulajdonságainak megjelenítése, mint például a méret, az engedélyek, a létrehozás és a hozzáférés dátuma többek között címkék nélkül:

`stat --terse {{path/to/file}}`

- Információk megjelenítése a fájlrendszerről, ahol egy adott fájl található:

`stat --file-system {{path/to/file}}`

- Csak nyolcjegyű fájlengedélyek megjelenítése:

`stat --format="%a %n" {{path/to/file}}`

- Egy adott fájl tulajdonosának és csoportjának megjelenítése:

`stat --format="%U %G" {{path/to/file}}`

- Egy adott fájl méretének megjelenítése bájtokban:

`stat --format="%s %n" {{path/to/file}}`
