# shc

> Általános shell script fordító. További információ: <https://manned.org/shc>.

- Shell szkript fordítása:

`shc -f {{script}}`

- Egy héjszkript fordítása és egy kimeneti bináris fájl megadása:

`shc -f {{script}} -o {{binary}}`

- Shell-szkript fordítása és a végrehajtható fájl lejárati dátumának beállítása:

`shc -f {{script}} -e {{dd/mm/yyyy}}`

- Héjszkript fordítása és a lejáratkor megjelenítendő üzenet beállítása:

`shc -f {{script}} -e {{dd/mm/yyyy}} -m "{{Please contact your provider}}"`
