# keepassxc-cli

> A KeepassXC parancssori interfésze. További információ: <https://manned.org/keepassxc-cli>.

- Keresési bejegyzések:

`keepassxc-cli lookup {{path/to/database_file}} {{name}}`

- Egy mappa tartalmának listázása:

`keepassxc-cli ls {{path/to/database_file}} {{/path/to/directory}}`

- Bejegyzés hozzáadása automatikusan generált jelszóval:

`keepassxc-cli add --generate {{path/to/database_file}} {{entry_name}}`

- Bejegyzés törlése:

`keepassxc-cli rm {{path/to/database_file}} {{entry_name}}`

- Egy bejegyzés jelszavának másolása a vágólapra:

`keepassxc-cli clip {{path/to/database_file}} {{entry_name}}`

- TOTP-kód másolása a vágólapra:

`keepassxc-cli clip --totp {{path/to/database_file}} {{entry_name}}`

- Jelszógenerálás 7 szóból álló jelszóval:

`keepassxc-cli diceware --words {{7}}`

- Jelszó generálása 16 nyomtatható ASCII karakterrel:

`keepassxc-cli generate --lower --upper --numeric --special --length {{16}}`
