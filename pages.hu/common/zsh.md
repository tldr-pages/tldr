# zsh

> Z SHell, egy Bash-kompatibilis parancssor-értelmező, lásd még: `bash`, `histexpand`. További információ: [https://www.zsh.org.](https://www.zsh.org)

- Interaktív shell munkamenet indítása:

`zsh`

- Konkrét \[c\]ommandók végrehajtása:

`zsh -c "{{echo Hello world}}"`

- Egy adott szkript végrehajtása:

`zsh {{path/to/script.zsh}}`

- Egy adott szkript ellenőrzése szintaktikai hibák szempontjából anélkül, hogy végrehajtaná azt:

`zsh --no-exec {{path/to/script.zsh}}`

- Konkrét parancsok végrehajtása az stdin-ből:

`{{echo Hello world}} | zsh`

- Egy adott parancsfájl végrehajtása, a parancsfájl minden egyes parancsának kinyomtatása a végrehajtás előtt:

`zsh --xtrace {{path/to/script.zsh}}`

- Interaktív shell munkamenet indítása verbózus módban, minden parancsot kinyomtatva a végrehajtás előtt:

`zsh --verbose`

- Egy adott parancs végrehajtása a `zsh` oldalon belül, letiltott glob-mintákkal:

`noglob {{command}}`
