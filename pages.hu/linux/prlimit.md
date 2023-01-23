# prlimit

> A folyamat erőforrásainak puha és kemény korlátjainak lekérdezése vagy beállítása. A prlimit egy folyamat azonosítóját és egy vagy több erőforrást megadva megpróbálja lekérdezni és/vagy módosítani a korlátokat. További információ: <https://manned.org/prlimit>.

- A futó szülőfolyamat összes aktuális erőforrásának határértékeinek megjelenítése:

`prlimit`

- Egy megadott folyamat összes aktuális erőforrásának határértékeinek megjelenítése:

`prlimit --pid {{pid number}}`

- Parancs futtatása a megnyitott fájlok egyéni számának korlátozásával:

`prlimit --nofile={{10}} {{command}}`
