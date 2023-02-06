# prctl

> A futó folyamatok, feladatok és projektek erőforrás-szabályozásának lekérése vagy beállítása. További információ: <https://www.unix.com/man-page/sunos/1/prctl>.

- Folyamathatárok és engedélyek vizsgálata:

`prctl {{pid}}`

- Folyamathatárok és engedélyek vizsgálata gépileg értelmezhető formátumban:

`prctl -P {{pid}}`

- Egy futó folyamat konkrét határértékének lekérdezése:

`prctl -n process.max-file-descriptor {{pid}}`
