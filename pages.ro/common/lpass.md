# lpass

> Interfață linie de comandă pentru managerul de parole LastPass.
> Mai multe informaţii: <https://github.com/lastpass/lastpass-cli>

- Conectați-vă la contul dvs. LastPass, introducând parola principală atunci când vi se solicită:

`lpass login {{username}}`

- Afișează starea de autentificare:

`lpass status`

- Listează toate site-urile grupate după categorie:

`lpass ls`

- Generați o nouă parolă pentru gmail.com cu identificatorul `myinbox` și adăugați la LastPass:

`lpass generate --username {{username}} --url {{gmail.com}} {{myinbox}} {{password_length}}`

- Afișați parola pentru o intrare specificată:

`lpass show {{myinbox}} --password`
