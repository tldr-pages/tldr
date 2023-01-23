# veracrypt

> Ingyenes és nyílt forráskódú lemez titkosító szoftver. További információ: <https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>.

- Új kötet létrehozása egy szöveges felhasználói felületen keresztül, és a `/dev/urandom` használata a véletlenszerű adatok forrásaként:

`veracrypt --text --create --random-source={{/dev/urandom}}`

- Egy kötet visszafejtése interaktív módon egy szöveges felhasználói felületen keresztül, és csatolása egy könyvtárba:

`veracrypt --text {{path/to/volume}} {{path/to/mount_point}}`

- Egy partíció visszafejtése egy kulcsfájl segítségével és csatolása egy könyvtárba:

`veracrypt --keyfiles={{path/to/keyfile}} {{/dev/sdXN}} {{path/to/mount_point}}`

- Egy kötet leválasztása a könyvtárban, amelybe fel van szerelve:

`veracrypt --dismount {{path/to/mounted_point}}`
