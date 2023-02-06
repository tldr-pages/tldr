# yank

> Beolvassa a bevitelt a `stdin` oldalról, és megjelenít egy kiválasztási felületet, amely lehetővé teszi egy mező kiválasztását és a vágólapra másolását. További információ: <https://manned.org/yank>.

- Kihúzás az alapértelmezett elválasztójelek (\\f, \\n, \\r, \\s, \\t) használatával:

`{{sudo dmesg}} | yank`

- Egy teljes sor kitépése:

`{{sudo dmesg}} | yank -l`

- Kihúzás egy adott elválasztójel használatával:

`{{echo hello=world}} | yank -d {{=}}`

- Csak az adott mintának megfelelő mezők törlése:

`{{ps ux}} | yank -g "{{[0-9]+}}"`
