# btrfs balance

> Blokkcsoportok kiegyensúlyozása egy btrfs fájlrendszerben. További információ: <https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>.

- A futó vagy szüneteltetett egyensúlyozási művelet állapotának megjelenítése:

`sudo btrfs balance status {{path/to/btrfs_filesystem}}`

- Minden blokkcsoport kiegyensúlyozása (lassú; újraírja az összes blokkot a fájlrendszerben):

`sudo btrfs balance start {{path/to/btrfs_filesystem}}`

- Kiegyensúlyozza a 15%-nál kisebb kihasználtságú adatblokkcsoportokat, a művelet a háttérben fut:

`sudo btrfs balance start --bg -dusage={{15}} {{path/to/btrfs_filesystem}}`

- Legfeljebb 10 metaadatfájlcsoport kiegyensúlyozása, amelyek kihasználtsága 20%-nál kisebb, és legalább 1 fájlcsoport egy adott eszközön: `devid` (lásd `btrfs filesystem show`):

`sudo btrfs balance start -musage={{20}},limit={{10}},devid={{devid}} {{path/to/btrfs_filesystem}}`

- Az adatblokkokat a raid6-ra, a metaadatokat pedig a raid1c3-ra konvertálja (lásd az mkfs.btrfs(8) profilokat):

`sudo btrfs balance start -dconvert={{raid6}} -mconvert={{raid1c3}} {{path/to/btrfs_filesystem}}`

- Adatblokkok konvertálása raid1-re, a már konvertált darabok kihagyásával (pl. egy korábbi, törölt konvertálási művelet után):

`sudo btrfs balance start -dconvert={{raid1}},soft {{path/to/btrfs_filesystem}}`

- Folyamatban lévő vagy szüneteltetett kiegyenlítési művelet törlése, szüneteltetése vagy folytatása:

`sudo btrfs balance {{cancel|pause|resume}} {{path/to/btrfs_filesystem}}`
