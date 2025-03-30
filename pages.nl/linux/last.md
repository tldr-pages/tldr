# last

> Toon informatie over de laatste gebruikerslogins.
> Bekijk ook: `lastb`, `login`.
> Meer informatie: <https://manned.org/last>.

- Toon logininformatie (bijv. gebruikersnaam, terminal, opstarttijd, kernel) van alle gebruikers:

`last`

- Toon logininformatie van een specifieke gebruiker:

`last {{gebruikersnaam}}`

- Toon informatie van een specifieke TTY:

`last {{tty1}}`

- Toon de meest recente informatie (standaard staan de nieuwste bovenaan):

`last | tac`

- Toon informatie over systeemopstarts:

`last "{{system boot}}"`

- Toon informatie met een specifiek [t]ijdstempel formaat:

`last --time-format {{notime|full|iso}}`

- Toon informatie [s]inds een specifieke tijd en datum:

`last --since {{-7days}}`

- Toon informatie (bijv. hostnaam en IP) van externe hosts:

`last --dns`
