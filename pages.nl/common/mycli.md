# mycli

> Een command-line client voor MySQL die automatische aanvulling en syntaxisaccentuering kan uitvoeren.
> Meer informatie: <https://mycli.net>.

- Verbinden met een lokale database op poort 3306, met de gebruikersnaam van de huidige gebruiker:

`mycli {{database_naam}}`

- Verbinden met een database (gebruiker wordt gevraagd om een wachtwoord):

`mycli -u {{gebruikersnaam}} {{database_naam}}`

- Verbinden met een database op een andere host:

`mycli -h {{database_host}} -P {{poort}} -u {{gebruikersnaam}} {{database_naam}}`
