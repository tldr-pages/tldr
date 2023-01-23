# safe

> CLI a HashiCorp Vault-tal való interakcióhoz. További információ: <https://github.com/starkandwayne/safe>.

- Biztonságos célpont hozzáadása:

`safe target {{vault_addr}} {{target_name}}`

- Hitelesítse a CLI-ügyfelet a Vault-kiszolgálóval szemben egy hitelesítési token segítségével:

`safe auth {{authentication_token}}`

- Nyomtassa ki az aktuális célpontot leíró környezeti változókat:

`safe env`

- Egy adott elérési útvonal összes elérhető kulcsának fahierarchiájának megjelenítése:

`safe tree {{path}}`

- Titok áthelyezése egyik útvonalról a másikra:

`safe move {{old/path/to/secret}} {{new/path/to/secret}}`

- Új 2048 bites SSH kulcspár generálása és tárolása:

`safe ssh {{2048}} {{path/to/secret}}`

- Nem érzékeny kulcsok beállítása egy titokhoz:

`safe set {{path/to/secret}} {{key}}={{value}}`

- Automatikusan generált jelszó beállítása egy titokban:

`safe gen {{path/to/secret}} {{key}}`
