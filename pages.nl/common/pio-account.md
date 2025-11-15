# pio account

> Beheer jouw PlatformIO account op de command-line.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/account/>.

- Registreer een nieuw PlatformIO account:

`pio account register {{[-u|--username]}} {{gebruikersnaam}} {{[-e|--email]}} {{email}} {{[-p|--password]}} {{wachtwoord}} --firstname {{voornaam}} --lastname {{achternaam}}`

- Verwijder permanent je PlatformIO account en gerelateerde data:

`pio account destroy`

- Log in bij je PlatformIO account:

`pio account login {{[-u|--username]}} {{gebruikersnaam}} {{[-p|--password]}} {{wachtwoord}}`

- Log uit bij je PlatformIO account:

`pio account logout`

- Update je PlatformIO profiel:

`pio account update {{[-u|--username]}} {{gebruikersnaam}} {{[-e|--email]}} {{email}} --firstname {{voornaam}} --lastname {{achternaam}} --current-password {{wachtwoord}}`

- Toon gedetailleerde informatie over je PlatformIO account:

`pio account show`

- Reset je wachtwoord door gebruik te maken van je gebruikersnaam of email:

`pio account forgot {{[-u|--username]}} {{gebruikersnaam_of_email}}`
