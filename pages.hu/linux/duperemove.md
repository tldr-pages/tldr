# duperemove

> Megkeresi a duplikált fájlrendszer-kiterjesztéseket, és opcionálisan ütemezi őket deduplikációra. A kiterjesztés egy fájl kis része a fájlrendszeren belül. Egyes fájlrendszereken egy kiterjesztésre többször is lehet hivatkozni, ha a fájlok tartalmának egy része azonos. További információ: <https://markfasheh.github.io/duperemove/>.

- Duplikált kiterjesztések keresése és megjelenítése egy könyvtárban:

`duperemove -r {{path/to/directory}}`

- Duplikált extentek deduplikálása Btrfs vagy XFS (kísérleti) fájlrendszeren:

`duperemove -r -d {{path/to/directory}}`

- Hash fájl használata a kiterjedési hash-ok tárolására (kisebb memóriahasználat és újra felhasználható a későbbi futtatások során):

`duperemove -r -d --hashfile={{path/to/hashfile}} {{path/to/directory}}`

- Korlátozza az I/O szálakat (a hashing és a dedupe szakaszhoz) és a CPU szálakat (a duplikált kiterjedések keresési szakaszához):

`duperemove -r -d --hashfile={{path/to/hashfile}} --io-threads={{N}} --cpu-threads={{N}} {{path/to/directory}}`
