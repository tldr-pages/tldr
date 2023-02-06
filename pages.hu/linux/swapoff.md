# swapoff

> Letiltja az eszköz vagy fájl cseréjét. További információ: <https://manned.org/swapoff>.

- Egy adott swap partíció letiltása:

`swapoff {{/dev/sdb7}}`

- Egy adott swap-fájl letiltása:

`swapoff {{path/to/file}}`

- Az összes swapterület letiltása:

`swapoff -a`

- A swap letiltása egy eszköz vagy fájl címkéje alapján:

`swapoff -L {{swap1}}`
