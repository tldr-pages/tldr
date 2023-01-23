# sherlock

> Felhasználónevek keresése a közösségi hálózatokon. További információ: <https://github.com/sherlock-project/sherlock>.

- Egy adott felhasználónév keresése a közösségi hálózatokon, az eredmények mentése egy fájlba:

`sherlock {{username}} --output {{path/to/file}}`

- Konkrét felhasználónevek keresése a közösségi hálózatokon az eredmények mentése egy könyvtárba:

`sherlock {{username1 username2 ...}} --folderoutput {{path/to/directory}}`

- Egy adott felhasználónév keresése a közösségi hálózatokon a Tor-hálózat segítségével:

`sherlock --tor {{username}}`

- A Toron keresztül történő lekérdezés minden egyes lekérdezés után új Tor-áramkörrel:

`sherlock --unique-tor {{username}}`

- Egy adott felhasználónév keresése a közösségi hálózatokon proxy használatával:

`sherlock {{username}} --proxy {{proxy_url}}`

- Egy adott felhasználónév keresése a közösségi hálózatokon és az eredmények megnyitása az alapértelmezett webböngészőben:

`sherlock {{username}} --browse`

- Súgó megjelenítése:

`sherlock --help`
