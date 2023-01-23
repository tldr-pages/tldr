# tail

> Egy fájl utolsó részének megjelenítése. Lásd még: `head`. További információ: <https://www.gnu.org/software/coreutils/tail>.

- A fájl utolsó 'count' sorainak megjelenítése:

`tail --lines {{count}} {{path/to/file}}`

- A fájl nyomtatása egy adott sorszámtól kezdődően:

`tail --lines +{{count}} {{path/to/file}}`

- Egy adott fájl végétől számított meghatározott számú bájt kiírása:

`tail --bytes {{count}} {{path/to/file}}`

- Egy adott fájl utolsó sorainak kiírása és a fájl olvasásának folytatása a `Ctrl + C`:

`tail --follow {{path/to/file}}`

- A fájl olvasásának folytatása a `Ctrl + C` címig, még akkor is, ha a fájl elérhetetlen:

`tail --retry --follow {{path/to/file}}`

- A "fájl" utolsó 'szám' sorainak megjelenítése és frissítés 'n' másodpercenként:

`tail --lines {{count}} --sleep-interval {{seconds}} --follow {{path/to/file}}`
