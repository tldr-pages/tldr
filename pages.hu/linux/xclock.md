# xclock

> Az idő megjelenítése analóg vagy digitális formában. További információ: <https://manned.org/xclock>.

- Analóg óra megjelenítése:

`xclock`

- 24 órás digitális óra megjelenítése csak az óra és a perc mezőkkel:

`xclock -digital -brief`

- Digitális óra megjelenítése strftime formátumú karakterlánc használatával (lásd strftime(3)):

`xclock -digital -strftime {{format}}`

- 24 órás digitális óra megjelenítése az óra, perc és másodperc mezőkkel, amely másodpercenként frissül:

`xclock -digital -strftime '%H:%M:%S' -update 1`

- 12 órás digitális óra megjelenítése csak az óra és perc mezőkkel:

`xclock -digital -twelve -brief`
