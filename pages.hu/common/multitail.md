# multitail

> A farok meghosszabbítása. További információ: <https://manned.org/multitail>.

- Az összes, egy mintának megfelelő fájl egy folyamban történő lefaragása:

`multitail -Q 1 '{{pattern}}'`

- Egy könyvtárban lévő összes fájl egy folyamban történő követése:

`multitail -Q 1 '{{path/to/directory}}/*'`

- Új fájlok automatikus hozzáadása egy ablakhoz:

`multitail -Q {{pattern}}`

- 5 naplófájl megjelenítése 2 összevonása közben, és 2 oszlopba helyezésük úgy, hogy csak egy legyen a bal oldali oszlopban:

`multitail -s 2 -sn 1,3 {{mergefile}} -I {{file1}} {{file2}} {{file3}} {{file4}}`
