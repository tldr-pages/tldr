# finger

> Programma voor het opzoeken van gebruikersinformatie.
> Meer informatie: <https://manned.org/finger>.

- Toon informatie over momenteel ingelogde gebruikers:

`finger`

- Toon informatie over een specifieke gebruiker:

`finger {{gebruikersnaam}}`

- Toon de loginnaam, echte naam, terminalnaam en andere informatie van de gebruiker:

`finger -s`

- Geef een output in meerdere regels weer met dezelfde informatie als `-s` evenals de thuisdirectory van de gebruiker, thuistelefoonnummer, loginshell, mailstatus, enz.:

`finger -l`

- Voorkom het matchen tegen gebruikersnamen en gebruik alleen login namen:

`finger -m`
