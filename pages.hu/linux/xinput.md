# xinput

> A rendelkezésre álló beviteli eszközök listázása, az eszközzel kapcsolatos információk lekérdezése és a beviteli eszköz beállításainak módosítása. További információ: <https://manned.org/xinput>.

- Az összes bemeneti eszköz listázása:

`xinput list`

- Egy bemenet letiltása:

`xinput disable {{id}}`

- Engedélyezzen egy bemenetet:

`xinput enable {{id}}`

- Egy bemenet leválasztása a mesteréről:

`xinput float {{id}}`

- Egy bemenet újracsatolása szolgaként a mesterhez:

`xinput reattach {{id}} {{master_id}}`

- Egy bemeneti eszköz beállításainak listázása:

`xinput list-props {{id}}`

- Egy bemeneti eszköz beállításainak módosítása:

`xinput set-prop {{id}} {{setting_id}} {{value}}`
