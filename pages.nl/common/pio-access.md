# pio access

> Stel het toegangsniveau in op publieke bronnen (pakketten) in het register.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/access/>.

- Verleen een gebruiker toegang tot een bron:

`pio access grant {{guest|maintainer|admin}} {{gebruikersnaam}} {{bron_urn}}`

- Verwijder de toegang voor een gebruiker tot een bron:

`pio access revoke {{gebruikersnaam}} {{bron_urn}}`

- Toon alle bronnen waartoe een gebruiker of team toegang tot heeft en het toegangsniveau:

`pio access list {{gebruikersnaam}}`

- Beperk de toegang tot een bron voor specifieke gebruikers of teamleden:

`pio access private {{bron_urn}}`

- Verleen alle gebruikers toegang tot een bron:

`pio access public {{bron_urn}}`
