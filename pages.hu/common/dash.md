# dash

> Debian Almquist Shell, a `sh` modern, POSIX-kompatibilis implementációja (nem Bash-kompatibilis). További információ: <https://manned.org/dash>.

- Indítson el egy interaktív shell munkamenetet:

`dash`

- Konkrét \[c\]ommandók végrehajtása:

`dash -c "{{echo 'dash is executed'}}"`

- Egy adott szkript végrehajtása:

`dash {{path/to/script.sh}}`

- Egy adott szkript ellenőrzése szintaktikai hibák szempontjából:

`dash -n {{path/to/script.sh}}`

- Egy adott szkript végrehajtása, miközben minden egyes parancsot kinyomtat a végrehajtás előtt:

`dash -x {{path/to/script.sh}}`

- Egy adott szkript végrehajtása és megállítás az első \[e\]rror esetén:

`dash -e {{path/to/script.sh}}`

- Konkrét parancsok végrehajtása a `stdin` oldalról:

`{{echo "echo 'dash is executed'"}} | dash`
