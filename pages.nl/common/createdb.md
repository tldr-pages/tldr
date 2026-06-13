# createdb

> Maak een PostgreSQL-database aan.
> Meer informatie: <https://www.postgresql.org/docs/current/app-createdb.html>.

- Maak een database aan die eigendom is van de huidige gebruiker:

`createdb {{database_naam}}`

- Maak een database aan die eigendom is van een specifieke gebruiker met een omschrijving:

`createdb {{[-O|--owner]}} {{gebruikersnaam}} {{database_naam}} '{{omschrijving}}'`

- Maak een database aan op basis van een template:

`createdb {{[-T|--template]}} {{template_naam}} {{database_naam}}`
