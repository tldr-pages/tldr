# usermod

> Wijzig een gebruikersaccount.
> Bekijk ook: `users`, `useradd`, `userdel`.
> Meer informatie: <https://manned.org/usermod>.

- Verander een gebruikersnaam:

`sudo usermod --login {{nieuwe_gebruikersnaam}} {{gebruikersnaam}}`

- Verander een gebruikers-ID:

`sudo usermod --uid {{id}} {{gebruikersnaam}}`

- Verander een gebruikersshell:

`sudo usermod --shell {{pad/naar/shell}} {{gebruikersnaam}}`

- Voeg een gebruiker toe aan aanvullende groepen (let op het ontbreken van spaties):

`sudo usermod --append --groups {{groep1,groep2,...}} {{gebruikersnaam}}`

- Verander een gebruikers thuismap:

`sudo usermod --move-home --home {{pad/naar/nieuwe_thuismap}} {{gebruikersnaam}}`
