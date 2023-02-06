# tailscale up

> Csatlakoztatja a klienst a Tailscale hálózathoz. 1.8-as és újabb verziókban a parancssori argumentumok tárolódnak és újra felhasználásra kerülnek, amíg felül nem írják őket, vagy meg nem hívják a `--reset` -t. További információ: <https://tailscale.com/kb/admin/>.

- Csatlakozás a Tailscale-hez:

`sudo tailscale up`

- Csatlakozik és felajánlja az aktuális gépet az internetes forgalom kilépési csomópontjának:

`sudo tailscale up --advertise-exit-node`

- Csatlakozás egy adott csomópont használatával az internetes forgalomhoz:

`sudo tailscale up --exit-node={{exit_node_ip}}`

- Csatlakozás és a bejövő kapcsolatok blokkolása az aktuális csomóponthoz:

`sudo tailscale up --shields-up`

- Csatlakozni és nem elfogadni a DNS konfigurációt az admin panelről (alapértelmezett beállítás: `true`):

`sudo tailscale up --accept-dns={{false}}`

- Csatlakozás és a Tailscale alhálózati útválasztóként történő konfigurálása:

`sudo tailscale up --advertise-routes={{10.0.0.0/24}},{{10.0.1.0/24}}`

- Csatlakozás és alhálózati útvonalak elfogadása a Tailscale-től:

`sudo tailscale up --accept-routes`

- Állítsa vissza a nem meghatározott beállításokat az alapértelmezett értékekre, és csatlakozzon:

`sudo tailscale up --reset`
