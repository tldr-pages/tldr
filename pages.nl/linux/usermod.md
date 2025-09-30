# usermod

> Wijzig een gebruikersaccount.
> Zie ook: `users`, `useradd`, `userdel`.
> Meer informatie: <https://manned.org/usermod>.

- Verander een gebruikersnaam:

`sudo usermod {{[-l|--login]}} {{nieuwe_gebruikersnaam}} {{gebruikersnaam}}`

- Verander een gebruikers-ID:

`sudo usermod {{[-u|--uid]}} {{id}} {{gebruikersnaam}}`

- Verander een gebruikersshell:

`sudo usermod {{[-s|--shell]}} {{pad/naar/shell}} {{gebruikersnaam}}`

- Voeg een gebruiker toe aan aanvullende groepen (let op het ontbreken van spaties):

`sudo usermod {{[-aG|--append --groups]}} {{groep1,groep2,...}} {{gebruikersnaam}}`

- Verwijder een gebruiker uit specifieke groepen:

`sudo usermod {{[-rG|--remove --groups]}} {{groep1,groep2,...}} {{gebruikersnaam}}`

- Verander een gebruikers thuismap:

`sudo usermod {{[-m|--move-home]}} {{[-d|--home]}} {{pad/naar/nieuwe_thuismap}} {{gebruikersnaam}}`

- Vergrendel een account:

`sudo usermod {{[-L|--lock]}} {{gebruikersnaam}}`

- Ontgrendel een account:

`sudo usermod {{[-U|--unlock]}} {{gebruikersnaam}}`
