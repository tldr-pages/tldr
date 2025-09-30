# su

> Wissel shell naar een andere gebruiker.
> Meer informatie: <https://manned.org/su>.

- Wissel naar superuser (vereist het root wachtwoord):

`su`

- Wissel naar een gegeven gebruiker (vereist het wachtwoord van de gebruiker):

`su {{gebruikersnaam}}`

- Wissel naar een gegeven gebruiker en simuleer een volledige login shell:

`su - {{gebruikersnaam}}`

- Voer een commando uit als een andere gebruiker:

`su - {{gebruikersnaam}} {{[-c|--command]}} "{{commando}}"`
