# transcrypt

> Criptați în mod transparent fișierele dintr-un depozit Git.
> Mai multe informaţii: <https://github.com/elasticdog/transcrypt>

- Inițializarea unui depozit neconfigurat:

`transcrypt`

- Listează fișierele criptate în prezent:

`git ls-crypt`

- Afișează acreditările unui depozit configurat:

`transcrypt --display`

- Inițializarea și decriptarea unei clone proaspete a unui depozit configurat:

`transcrypt --cipher={{cipher}}`

- Rekey pentru a schimba cifrul de criptare sau parola:

`transcrypt --rekey`
