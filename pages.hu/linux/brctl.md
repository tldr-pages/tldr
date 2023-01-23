# brctl

> Ethernet-híd adminisztráció. További információ: <https://manned.org/brctl>.

- A jelenleg létező Ethernet-hidakra vonatkozó információkat tartalmazó lista megjelenítése:

`sudo brctl show`

- Új Ethernet-híd interfész létrehozása:

`sudo brctl add {{bridge_name}}`

- Meglévő Ethernet-híd interfész törlése:

`sudo brctl del {{bridge_name}}`

- Interfész hozzáadása egy meglévő hídhoz:

`sudo brctl addif {{bridge_name}} {{interface_name}}`

- Interfész eltávolítása egy meglévő hídból:

`sudo brctl delif {{bridge_name}} {{interface_name}}`
