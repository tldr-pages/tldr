# valgrind

> A programok profilozására, optimalizálására és hibakeresésére szolgáló szakértői eszközök csomagolása. Gyakran használt eszközök: `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind` és `drd`. További információ: <http://www.valgrind.org>.

- A Memcheck (alapértelmezett) eszközzel a memóriahasználat diagnosztikáját a `program` mutatja meg:

`valgrind {{program}}`

- A Memcheck segítségével a `program` összes lehetséges memóriaszivárgását teljes részletességgel jelentheti:

`valgrind --leak-check=full --show-leak-kinds=all {{program}}`

- Használja a Cachegrind eszközt a `program` CPU gyorsítótár műveleteinek profilozásához és naplózásához:

`valgrind --tool=cachegrind {{program}}`

- A Massif eszközzel a `program` memóriakupac- és veremhasználatának profilja és naplózása:

`valgrind --tool=massif --stacks=yes {{program}}`
