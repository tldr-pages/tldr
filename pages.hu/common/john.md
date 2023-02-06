# john

> Jelszófeltörő. További információ: <https://www.openwall.com/john/>.

- Jelszóhashek feltörése:

`john {{path/to/hashes.txt}}`

- Megmutatja a feltört jelszavakat:

`john --show {{path/to/hashes.txt}}`

- A felhasználók feltört jelszavainak megjelenítése felhasználói azonosító szerint több fájlból:

`john --show --users={{user_ids}} {{path/to/hashes*}} {{path/to/other/hashes*}}`

- Jelszóhasábok feltörése egyéni szólista használatával:

`john --wordlist={{path/to/wordlist.txt}} {{path/to/hashes.txt}}`

- A rendelkezésre álló hash-formátumok listája:

`john --list=formats`

- Jelszóhash-ok feltörése egy adott hash-formátum használatával:

`john --format={{md5crypt}} {{path/to/hashes.txt}}`

- Jelszóhashtömbök feltörése, a szómagyarázó szabályok engedélyezése:

`john --rules {{path/to/hashes.txt}}`

- Megszakított feltörési munkamenet visszaállítása egy állapotfájlból, pl. `mycrack.rec`:

`john --restore={{path/to/mycrack.rec}}`
