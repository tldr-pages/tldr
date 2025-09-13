# dropdb

> Verwijder een PostgreSQL-database.
> Een eenvoudige wrapper voor het SQL-commando `DROP DATABASE`.
> Meer informatie: <https://www.postgresql.org/docs/current/app-dropdb.html>.

- Verwijder een database:

`dropdb {{database_naam}}`

- Vraag om bevestiging voordat destructieve acties worden uitgevoerd:

`dropdb {{[-i|--interactive]}} {{database_naam}}`

- Maak verbinding als een specifieke gebruiker en verwijder een database:

`dropdb {{[-U|--username]}} {{gebruikersnaam}} {{database_naam}}`

- Forceer een wachtwoordprompt voordat er wordt verbonden met de database:

`dropdb {{[-W|--password]}} {{database_naam}}`

- Onderdruk een wachtwoordprompt voordat er wordt verbonden met de database:

`dropdb {{[-w|--no-password]}} {{database_naam}}`

- Specificeer de hostnaam van de server:

`dropdb {{[-h|--host]}} {{host}} {{database_naam}}`

- Specificeer de serverpoort:

`dropdb {{[-p|--port]}} {{poort}} {{database_naam}}`

- Probeer actieve verbindingen te verbreken voordat de database wordt vernietigd:

`dropdb {{[-f|--force]}} {{database_naam}}`
