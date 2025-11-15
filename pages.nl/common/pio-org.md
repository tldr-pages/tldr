# pio org

> Beheer PlatformIO organisaties en hun eigenaren.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/org/>.

- Maak een nieuwe organisatie:

`pio org create {{organisatie_naam}}`

- Verwijder een organisatie:

`pio org destroy {{organisatie_naam}}`

- Voeg een gebruiker toe aan een organisatie:

`pio org add {{organisatie_naam}} {{gebruikersnaam}}`

- Verwijder een gebruiker van een organisatie:

`pio org remove {{organisatie_naam}} {{gebruikersnaam}}`

- Toon alle organisaties waar de huidige gebruiker lid van is en de eigenaren:

`pio org list`

- Update de name, email of weergave naam van een organisatie:

`pio org update --orgname {{nieuwe_organisatie_naam}} --email {{nieuw_email}} --displayname {{nieuwe_weergave_naam}} {{organisatie_naam}}`
