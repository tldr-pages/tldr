# sysbench

> A rendszer CPU, IO és memória teljesítményének összehasonlítása. További információ: <https://github.com/akopytov/sysbench/>.

- Futtasson CPU benchmarkot 1 szálon 10 másodpercig:

`sysbench cpu run`

- CPU benchmark futtatása több szálon keresztül egy megadott ideig:

`sysbench --threads={{number_of_threads}} --time={{seconds}}`

- Memória benchmark futtatása 1 szálon 10 másodpercig:

`sysbench memory run`

- Készítsen elő egy fájlrendszer-szintű olvasási benchmarkot:

`sysbench fileio prepare`

- Fájlrendszer-szintű benchmark futtatása:

`sysbench --file-test-mode={{rndrd|rndrw|rndwr|seqrd|seqrewr|seqwr}} fileio run`
