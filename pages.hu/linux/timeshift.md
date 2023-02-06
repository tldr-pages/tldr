# timeshift

> Rendszer-visszaállítási segédprogram. További információ: <https://github.com/teejee2008/timeshift>.

- Pillanatképek listázása:

`sudo timeshift --list`

- Új pillanatfelvétel létrehozása (ha ütemezve van):

`sudo timeshift --check`

- Új pillanatfelvétel létrehozása (akkor is, ha nincs ütemezve):

`sudo timeshift --create`

- Pillanatfelvétel visszaállítása (interaktívan kiválasztva, hogy melyik pillanatfelvételt kívánja visszaállítani):

`sudo timeshift --restore`

- Egy adott pillanatfelvétel visszaállítása:

`sudo timeshift --restore --snapshot '{{snapshot}}'`

- Egy adott pillanatfelvétel törlése:

`sudo timeshift --delete --snapshot '{{snapshot}}'`
