# compgen

> Beépített parancs a Bash automatikus kitöltésére, amely a TAB billentyű kétszeri lenyomásakor hívódik. További információ: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- Sorolja fel az összes futtatható parancsot:

`compgen -c`

- List all aliasok listája:

`compgen -a`

- List all functions that you could run:

`compgen -A function`

- A shell fenntartott kulcsszavainak megjelenítése:

`compgen -k`

- Az összes elérhető parancs/alízis megtekintése az 'ls'-sel kezdődően:

`compgen -ac {{ls}}`
