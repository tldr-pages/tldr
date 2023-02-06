# parallel

> Parancsok futtatása több CPU-magon. További információ: <https://www.gnu.org/software/parallel>.

- Több fájl egyidejű gzipelése, az összes processzormag használatával:

`parallel gzip ::: {{file1}} {{file2}} {{file3}}`

- Érvek beolvasása a `stdin` oldalról , 4 feladat futtatása egyszerre:

`ls *.txt | parallel -j4 gzip`

- JPG képek átalakítása PNG-be a helyettesítő karakterláncok használatával:

`parallel convert {} {.}.png ::: *.jpg`

- Párhuzamos xargs, a lehető legtöbb argumentumot zsúfolja egy parancsba:

`{{args}} | parallel -X {{command}}`

- A `stdin` felbontása ~1M blokkokra, minden egyes blokk betáplálása az új parancs `stdin` címére:

`cat {{big_file.txt}} | parallel --pipe --block 1M {{command}}`

- Futtatás több gépen SSH-n keresztül:

`parallel -S {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}`
