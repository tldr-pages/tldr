# useradd

> Maak een nieuwe gebruiker aan.
> Bekijk ook: `users`, `userdel`, `usermod`.
> Meer informatie: <https://manned.org/useradd>.

- Maak een nieuwe gebruiker aan:

`sudo useradd {{gebruikersnaam}}`

- Maak een nieuwe gebruiker aan met de opgegeven gebruikers-ID:

`sudo useradd --uid {{id}} {{gebruikersnaam}}`

- Maak een nieuwe gebruiker aan met de opgegeven shell:

`sudo useradd --shell {{pad/naar/shell}} {{gebruikersnaam}}`

- Maak een nieuwe gebruiker aan die behoort tot extra groepen (let op het ontbreken van spaties):

`sudo useradd --groups {{groep1,groep2,...}} {{gebruikersnaam}}`

- Maak een nieuwe gebruiker aan met de standaard thuismap:

`sudo useradd --create-home {{gebruikersnaam}}`

- Maak een nieuwe gebruiker aan met de thuismap gevuld met bestanden uit een sjabloonmap:

`sudo useradd --skel {{pad/naar/sjabloonmap}} --create-home {{gebruikersnaam}}`

- Maak een nieuwe systeemgebruiker aan zonder thuismap:

`sudo useradd --system {{gebruikersnaam}}`
