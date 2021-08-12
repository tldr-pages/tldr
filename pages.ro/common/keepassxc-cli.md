# keepassxc-cli

> Interfață linie de comandă pentru KeePassXC.
> Mai multe informaţii: <https://manned.org/keepassxc-cli>

- Intrări de căutare:

`keepassxc-cli lookup {{path/to/database_file}} {{name}}`

- Listează conținutul unui dosar:

`keepassxc-cli ls {{path/to/database_file}} {{/path/to/directory}}`

- Adăugați o intrare cu o parolă generată automat:

`keepassxc-cli add --generate {{path/to/database_file}} {{entry_name}}`

- Şterge o intrare:

`keepassxc-cli rm {{path/to/database_file}} {{entry_name}}`

- Copiați parola unei intrări în clipboard:

`keepassxc-cli clip {{path/to/database_file}} {{entry_name}}`

- Copiați un cod TOTP în clipboard:

`keepassxc-cli clip --totp {{path/to/database_file}} {{entry_name}}`

- Generează o frază de acces cu 7 cuvinte:

`keepassxc-cli diceware --words {{7}}`

- Generarea unei parole cu 16 caractere ASCII imprimabile:

`keepassxc-cli generate --lower --upper --numeric --special --length {{16}}`
