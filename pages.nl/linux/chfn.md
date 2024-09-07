# chfn

> Werk de `finger`-informatie bij voor een gebruiker.
> Meer informatie: <https://manned.org/chfn>.

- Werk het "Naam"-veld van een gebruiker bij in de uitvoer van `finger`:

`chfn -f {{nieuwe_weergavenaam}} {{gebruikersnaam}}`

- Werk het "Kantoornummer"-veld van een gebruiker bij voor de uitvoer van `finger`:

`chfn -o {{nieuw_kantoornummer}} {{gebruikersnaam}}`

- Werk het "Kantoor Telefoonnummer"-veld van een gebruiker bij voor de uitvoer van `finger`:

`chfn -p {{nieuw_kantoor_telefoonnummer}} {{gebruikersnaam}}`

- Werk het "Thuis Telefoonnummer"-veld van een gebruiker bij voor de uitvoer van `finger`:

`chfn -h {{nieuw_thuis_telefoonnummer}} {{gebruikersnaam}}`
