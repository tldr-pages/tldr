# passwd

> Verander het wachtwoord van een gebruiker.
> Meer informatie: <https://manned.org/passwd>.

- Verander het wachtwoord van de huidige gebruiker interactief:

`passwd`

- Verander het wachtwoord van een specifieke gebruiker:

`passwd {{gebruikersnaam}}`

- Toon de huidige status van de gebruiker:

`passwd {{[-S|--status]}}`

- Maak het wachtwoord van het account leeg (hiermee wordt de opgegeven account wachtwoordloos):

`passwd {{[-d|--delete]}}`

- Stel het wachtwoord programmatisch in (handig voor installatiescripts):

`yes {{wachtwoord}} | passwd`
