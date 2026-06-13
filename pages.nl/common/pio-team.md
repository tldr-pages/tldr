# pio team

> Beheer PlatformIO teams.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/team/>.

- Maak een nieuw team met de gespecificeerde beschrijving:

`pio team create --description {{beschrijving}} {{organisatie_naam}}:{{team_naam}}`

- Verwijder een team:

`pio team destroy {{organisatie_naam}}:{{team_naam}}`

- Voeg een nieuwe gebruiker toe aan een team:

`pio team add {{organisatie_naam}}:{{team_naam}} {{gebruikersnaam}}`

- Verwijder een gebruiker uit een team:

`pio team remove {{organisatie_naam}}:{{team_naam}} {{gebruikersnaam}}`

- Toon alle teams waar de gebruiker lid van is en alle leden:

`pio team list`

- Toon alle teams in een organisatie:

`pio team list {{organisatie_naam}}`

- Hernoem een team:

`pio team update --name {{nieuwe_team_naam}} {{organisatie_naam}}:{{team_naam}}`

- Verander de beschrijving van een team:

`pio team update --description {{nieuwe_beschrijving}} {{organisatie_naam}}:{{team_naam}}`
