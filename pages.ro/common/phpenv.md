# phpenv

> Un manager de versiuni PHP în scopuri de dezvoltare.
> Mai multe informaţii: <https://github.com/phpenv/phpenv>

- Instalați o versiune PHP la nivel global:

`phpenv install {{version}}`

- Reîmprospătați fișierele shim pentru toate binarele PHP cunoscute de `phpenv`:

`phpenv rehash`

- Listează toate versiunile PHP instalate:

`phpenv versions`

- Afișează versiunea PHP activă în prezent:

`phpenv version`

- Setați versiunea globală PHP:

`phpenv global {{version}}`

- Setați versiunea PHP locală, care suprascrie versiunea globală:

`phpenv local {{version}}`

- Anulează versiunea PHP locală:

`phpenv local --unset`
