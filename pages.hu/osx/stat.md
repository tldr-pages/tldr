# stat

> A fájl állapotának megjelenítése. További információ: <https://ss64.com/osx/stat.html>.

- A fájl tulajdonságainak megjelenítése, mint például a méret, az engedélyek, a létrehozás és a hozzáférés dátuma:

`stat {{path/to/file}}`

- Ugyanaz, mint a fentiekben, de bővebben (inkább a Linux `stat`):

`stat -x {{path/to/file}}`

- Csak nyolcjegyű fájlengedélyek megjelenítése:

`stat -f %Mp%Lp {{path/to/file}}`

- A fájl tulajdonosának és csoportjának megjelenítése:

`stat -f "%Su %Sg" {{path/to/file}}`

- A fájl méretének megjelenítése bájtokban:

`stat -f "%z %N" {{path/to/file}}`
