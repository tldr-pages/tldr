# mycli

> Een CLI voor MySQL, MariaDB en Percona die automatische aanvulling en syntaxisaccentuering kan uitvoeren.
> Meer informatie: <https://manned.org/mycli>.

- Verbinden met een lokale database op poort 3306, met de gebruikersnaam van de huidige gebruiker:

`mycli {{database_naam}}`

- Verbinden met een database (gebruiker wordt gevraagd om een wachtwoord):

`mycli {{[-u|--user]}} {{gebruikersnaam}} {{database_naam}}`

- Verbinden met een database op een andere host:

`mycli {{[-h|--host]}} {{database_host}} {{[-P|--port]}} {{poort}} {{[-u|--user]}} {{gebruikersnaam}} {{database_naam}}`
