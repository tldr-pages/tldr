# debugfs

> Interaktív ext2/ext3/ext4 fájlrendszer hibakereső. További információ: <https://manned.org/debugfs>.

- A fájlrendszer megnyitása csak olvasási módban:

`debugfs {{/dev/sdXN}}`

- A fájlrendszer megnyitása író-olvasó módban:

`debugfs -w {{/dev/sdXN}}`

- Parancsok beolvasása egy megadott fájlból, azok végrehajtása, majd kilépés:

`debugfs -f {{path/to/cmd_file}} {{/dev/sdXN}}`

- A fájlrendszer statisztikáinak megtekintése a debugfs konzolon:

`stats`

- A fájlrendszer bezárása:

`close -a`

- Az összes elérhető parancs listázása:

`lr`
