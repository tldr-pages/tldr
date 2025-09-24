# adduser

> Hulpprogramma voor het aanmaken van gebruikers.
> Meer informatie: <https://manned.org/adduser>.

- Maak een nieuwe gebruiker aan met een standaard thuismap en vraag de gebruiker een wachtwoord in te stellen:

`adduser {{gebruikersnaam}}`

- Maak een nieuwe gebruiker aan zonder thuismap:

`adduser --no-create-home {{gebruikersnaam}}`

- Maak een nieuwe gebruiker aan met een thuismap op het opgegeven pad:

`adduser --home {{pad/naar/thuismap}} {{gebruikersnaam}}`

- Maak een gebruiker aan met de opgegeven shell als login-shell:

`adduser --shell {{pad/naar/shell}} {{gebruikersnaam}}`

- Maak een nieuwe gebruiker aan die tot de opgegeven groep behoort:

`adduser --ingroup {{groep}} {{gebruikersnaam}}`
