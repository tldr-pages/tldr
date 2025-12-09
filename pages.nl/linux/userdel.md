# userdel

> Verwijder een gebruikersaccount of verwijder een gebruiker uit een groep.
> Zie ook: `users`, `useradd`, `usermod`.
> Meer informatie: <https://manned.org/userdel>.

- Verwijder een gebruiker:

`sudo userdel {{gebruikersnaam}}`

- Verwijder een gebruiker in een andere root-map:

`sudo userdel {{[-R|--root]}} {{pad/naar/andere/root}} {{gebruikersnaam}}`

- Verwijder een gebruiker samen met de thuismap en mail-spool:

`sudo userdel {{[-r|--remove]}} {{gebruikersnaam}}`
