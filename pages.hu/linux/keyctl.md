# keyctl

> A Linux kernel kulcstartó manipulálása. További információ: <https://manned.org/keyctl>.

- Egy adott kulcstárban lévő kulcsok listázása:

`keyctl list {{target_keyring}}`

- A felhasználó alapértelmezett munkamenetében lévő aktuális kulcsok listázása:

`keyctl list {{@us}}`

- Kulcs tárolása egy adott kulcskarban:

`keyctl add {{type_keyring}} {{key_name}} {{key_value}} {{target_keyring}}`

- Egy kulcs tárolása a szabványos bemenetről származó értékével:

`echo -n {{key_value}} | keyctl padd {{type_keyring}} {{key_name}} {{target_keyring}}`

- Időkorlátozás beállítása egy kulcshoz:

`keyctl timeout {{key_name}} {{timeout_in_seconds}}`

- Kulcs beolvasása és hex-dump formátumban történő formázása, ha nem nyomtatható:

`keyctl read {{key_name}}`

- Kulcs beolvasása és formázása úgy, ahogy van:

`keyctl pipe {{key_name}}`

- Kulcs visszavonása és a kulcson végzett további műveletek megakadályozása:

`keyctl revoke {{key_name}}`
