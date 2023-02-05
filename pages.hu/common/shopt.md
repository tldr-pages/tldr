# shopt

> Bash shell opciók kezelése: olyan változók (tárolva a `$BASHOPTS`), amelyek a Bash shell specifikus viselkedését szabályozzák.
> Az általános POSIX shell változókat (tárolva a `$SHELLOPTS`) ehelyett a `set` paranccsal lehet kezelni.
> További információ: <https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html>.

- Az összes beállítható opció listája, és hogy be vannak-e állítva:

`shopt`

- Beállít egy opciót:

`shopt -s {{option_name}}`

- Egy opció beállításának feloldása:

`shopt -u {{option_name}}`

- Az összes opció és állapotuk listájának kiírása futtatható `shopt` parancsokként formázva:

`shopt -p`

- A parancs súgójának megjelenítése:

`help shopt`
