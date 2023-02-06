# tail

> Egy fájl utolsó részének megjelenítése. Lásd még: `head`. További információ: <https://manned.org/man/freebsd-13.0/tail.1>.

- A fájl utolsó 'count' sorainak megjelenítése:

`tail -n {{count}} {{path/to/file}}`

- A fájl nyomtatása egy adott sorszámtól kezdődően:

`tail -n +{{count}} {{path/to/file}}`

- Egy adott fájl végétől számított meghatározott számú bájt kiírása:

`tail -c {{count}} {{path/to/file}}`

- Egy adott fájl utolsó sorainak kiírása és a fájl olvasásának folytatása a `Ctrl + C`:

`tail -f {{path/to/file}}`

- A fájl olvasásának folytatása a `Ctrl + C` címig, még akkor is, ha a fájl elérhetetlen:

`tail -F {{path/to/file}}`

- A "file" utolsó "count" sorainak megjelenítése és frissítés minden "seconds" másodpercenként:

`tail -n {{count}} -s {{seconds}} -f {{path/to/file}}`
