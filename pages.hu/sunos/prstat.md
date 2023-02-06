# prstat

> Aktív folyamatok statisztikáinak jelentése. További információ: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Az összes folyamat vizsgálata és a CPU-használat szerint rendezett statisztikák jelentése:

`prstat`

- Az összes folyamat és jelentés statisztikájának vizsgálata memóriahasználat szerint rendezve:

`prstat -s rss`

- Teljes felhasználási összefoglaló jelentés minden egyes felhasználó számára:

`prstat -t`

- Mikroállapot-folyamatok elszámolási információinak jelentése:

`prstat -m`

- Másodpercenként kiírja a CPU-t leginkább használó 5 folyamat listáját:

`prstat -c -n 5 -s cpu 1`
