# monodevelop

> Platformokon átívelő IDE C#, F# és más nyelvekhez. További információ: <https://www.monodevelop.com/>.

- MonoDevelop indítása:

`monodevelop`

- Egy adott fájl megnyitása:

`monodevelop {{path/to/file}}`

- Egy adott fájl megnyitása a caret egy adott pozícióban történő megnyitásával:

`monodevelop {{path/to/file}};{{line_number}};{{column_number}}`

- Új ablak megnyitásának kikényszerítése a meglévő ablakra való váltás helyett:

`monodevelop --new-window`

- A `stdout` és a `stderr` átirányításának letiltása egy naplófájlba:

`monodevelop --no-redirect`

- Teljesítményfigyelés engedélyezése:

`monodevelop --perf-log`
