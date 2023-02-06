# fstrim

> Kizárólag a flashmemória-eszközök, például SSD-k és microSD-kártyák támogatják. További információ: <https://manned.org/fstrim>.

- A nem használt blokkok levágása minden olyan csatlakoztatott partíción, amely támogatja:

`sudo fstrim --all`

- A nem használt blokkok levágása egy megadott partíción:

`sudo fstrim {{/}}`

- Statisztikák megjelenítése a trimmelés után:

`sudo fstrim --verbose {{/}}`
