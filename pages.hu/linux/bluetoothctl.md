# bluetoothctl

> Bluetooth-eszközök kezelése a parancssorból. További információk: <https://bitbucket.org/serkanp/bluetoothctl>.

- Lépjen be a `bluetoothctl` parancsértelmezőbe:

`bluetoothctl`

- Listázza az összes ismert eszközt:

`bluetoothctl devices`

- Kapcsolja be vagy ki a Bluetooth-vezérlőt:

`bluetoothctl power {{on|off}}`

- Párosítás egy eszközzel:

`bluetoothctl pair {{mac_address}}`

- Egy eszköz eltávolítása:

`bluetoothctl remove {{mac_address}}`

- Csatlakozás egy párosított eszközhöz:

`bluetoothctl connect {{mac_address}}`

- A párosított eszközzel való kapcsolat megszakítása:

`bluetoothctl disconnect {{mac_address}}`

- Súgó megjelenítése:

`bluetoothctl help`
