# mpstat

> CPU-statisztikák jelentése. További információ: <https://manned.org/mpstat>.

- CPU-statisztikák megjelenítése 2 másodpercenként:

`mpstat {{2}}`

- 5 jelentés megjelenítése, egyenként, 2 másodperces időközönként:

`mpstat {{2}} {{5}}`

- Egy adott processzorról 5 jelentés megjelenítése, egyenként, 2 másodperces időközönként:

`mpstat -P {{0}} {{2}} {{5}}`
