# lxc

> Linux konténerek kezelése az lxd REST API segítségével. Bármely konténer nevéhez vagy mintájához előtagként megadható a távoli kiszolgáló neve. További információ: <https://manned.org/lxc>.

- Egy karakterláncnak megfelelő helyi konténerek listázása. A karakterlánc elhagyásával az összes helyi konténer listázható:

`lxc list {{match_string}}`

- Egy stringre illeszkedő képek listázása. Az összes kép listázásához hagyja ki a karakterláncot:

`lxc image list [{{remote}}:]{{match_string}}`

- Új konténer létrehozása egy képből:

`lxc init [{{remote}}:]{{image}} {{container}}`

- Konténer indítása:

`lxc start [{{remote}}:]{{container}}`

- Konténer leállítása:

`lxc stop [{{remote}}:]{{container}}`

- Részletes információk megjelenítése a konténerről:

`lxc info [{{remote}}:]{{container}}`

- Pillanatkép készítése egy konténerről:

`lxc snapshot [{{remote}}:]{{container}} {{snapshot}}`

- Egy adott parancs végrehajtása egy konténeren belül:

`lxc exec [{{remote}}:]{{container}} {{command}}`
