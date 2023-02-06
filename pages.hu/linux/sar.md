# sar

> A különböző Linux alrendszerek teljesítményének figyelése. További információ: <https://manned.org/sar>.

- Jelentse a fizikai eszközökre kiadott I/O és átviteli sebességet, másodpercenként egyet (kilépéshez nyomja meg a CTRL+C billentyűkombinációt):

`sar -b {{1}}`

- Összesen 10 hálózati eszközstatisztika jelentése, 2 másodpercenként egy:

`sar -n DEV {{2}} {{10}}`

- CPU-kihasználtsági jelentés, 2 másodpercenként egy:

`sar -u ALL {{2}}`

- Összesen 20 memóriakihasználtsági statisztika jelentése, másodpercenként egy:

`sar -r ALL {{1}} {{20}}`

- Jelentse a futási sor hosszát és a terhelés átlagát, másodpercenként egyet:

`sar -q {{1}}`

- Lapozási statisztikák jelentése, 5 másodpercenként egy:

`sar -B {{5}}`
