# swapon

> Engedélyezi az eszköz vagy fájl cseréjét. További információ: <https://manned.org/swapon>.

- Swap-információk lekérése:

`swapon -s`

- Egy adott swap partíció engedélyezése:

`swapon {{/dev/sdb7}}`

- Egy adott swap-fájl engedélyezése:

`swapon {{path/to/file}}`

- Az összes swapterület engedélyezése:

`swapon -a`

- A swap engedélyezése egy eszköz vagy fájl címkéje alapján:

`swapon -L {{swap1}}`
