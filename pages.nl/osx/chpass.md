# chpass

> Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
> Let op: het is niet mogelijk om een gebruikerswachtwoord te wijzigen op een Open Directory systeem, gebruik hiervoor `passwd`.
> Bekijk ook: `passwd`.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Voeg toe of pas interactief de gebruikersdatabase informatie aan voor de huidige gebruiker:

`su -c chpass`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`chpass -s {{pad/naar/shell}}`

- Stel een login [s]hell in voor een specifieke gebruiker:

`chpass -s {{pad/naar/shell}} {{gebruikersnaam}}`

- Pas het gebruikersrecord aan in de directory node op de opgegeven [l]ocatie:

`chpass -l {{locatie}} -s {{pad/naar/shell}} {{gebruikersnaam}}`

- Gebruik de opgegeven gebr[u]ikersnaam bij het authenticeren van het mapknooppunt dat de gebruiker bevat:

`chpass -u {{auth_naam}} -s {{pad/naar/shell}} {{gebruikersnaam}}`
