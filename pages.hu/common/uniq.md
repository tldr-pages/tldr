# uniq

> Az egyedi sorok kimenete a megadott bemenetből vagy fájlból. Mivel az ismétlődő sorokat csak akkor érzékeli, ha azok egymás mellett vannak, ezért először rendezni kell őket. További információ: <https://www.gnu.org/software/coreutils/uniq>.

- Minden sort egyszer jelenít meg:

`sort {{path/to/file}} | uniq`

- Csak az egyedi sorokat jeleníti meg:

`sort {{path/to/file}} | uniq -u`

- Csak a duplikált sorok megjelenítése:

`sort {{path/to/file}} | uniq -d`

- Az egyes sorok előfordulási számának megjelenítése az adott sorral együtt:

`sort {{path/to/file}} | uniq -c`

- Az egyes sorok előfordulási számának megjelenítése a leggyakoribbak szerint rendezve:

`sort {{path/to/file}} | uniq -c | sort -nr`
