# psql

> PostgreSQL-client.
> Meer informatie: <https://www.postgresql.org/docs/current/app-psql.html>.

- Maak verbinding met de database. Standaard wordt er verbinding gemaakt met de lokale socket op poort 5432 met de huidig ingelogde gebruiker:

`psql {{database}}`

- Maak verbinding met de database op de opgegeven serverhost die draait op de opgegeven poort met de opgegeven gebruikersnaam, zonder een wachtwoordprompt:

`psql {{[-h|--host]}} {{host}} {{[-p|--port]}} {{poort}} {{[-U|--username]}} {{gebruikersnaam}} {{database}}`

- Maak verbinding met de database, waarbij aan de gebruiker om een wachtwoord wordt gevraagd:

`psql {{[-h|--host]}} {{host}} {{[-p|--port]}} {{poort}} {{[-U|--username]}} {{gebruikersnaam}} {{[-W|--password]}} {{database}}`

- Voer één SQL-query of PostgreSQL-commando uit op de opgegeven database (handig in shell-scripts):

`psql {{[-c|--command]}} '{{query}}' {{database}}`

- Voer commando's vanuit een bestand uit op de opgegeven database:

`psql {{database}} {{[-f|--file]}} {{pad/naar/bestand.sql}}`
