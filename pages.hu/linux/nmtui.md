# nmtui

> Szöveges felhasználói felület a NetworkManager vezérlésére. A navigáláshoz használja a nyílbillentyűket, az opció kiválasztásához pedig az enter-t. További információ: <https://networkmanager.dev/docs/api/latest/nmtui.html>.

- Nyissa meg a felhasználói felületet:

`nmtui`

- A rendelkezésre álló kapcsolatok listájának megjelenítése, az aktiválás vagy deaktiválás lehetőségével:

`nmtui connect`

- Csatlakozás egy adott hálózathoz:

`nmtui connect {{name|uuid|device|SSID}}`

- Adott hálózat szerkesztése/hozzáadása/törlése:

`nmtui edit {{name|id}}`

- A rendszer hostnevének beállítása:

`nmtui hostname`
