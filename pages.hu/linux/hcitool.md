# hcitool

> A kapcsolatok figyelése, konfigurálása és speciális parancsok küldése Bluetooth-eszközöknek. További információk: <https://manned.org/hcitool>.

- Bluetooth-eszközök keresése:

`hcitool scan`

- Egy eszköz nevének kiadása, visszaadva annak MAC-címét:

`hcitool name {{bdaddr}}`

- Információk lekérése egy távoli Bluetooth-eszközről:

`hcitool info {{bdaddr}}`

- A Bluetooth-eszközzel való kapcsolat minőségének ellenőrzése:

`hcitool lq {{bdaddr}}`

- Az átviteli teljesítményszint módosítása:

`hcitool tpl {{bdaddr}} {{0|1}}`

- A kapcsolati házirend megjelenítése:

`hcitool lp`

- Hitelesítés kérése egy adott eszközzel:

`hcitool auth {{bdaddr}}`

- Helyi eszközök megjelenítése:

`hcitool dev`
