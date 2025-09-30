# mssqlclient.py

> Maak verbinding met Microsoft SQL Server instanties en voer queries uit.
> Onderdeel van de Impacket-suite.
> Meer informatie: <https://github.com/fortra/impacket>.

- Maak verbinding met een MSSQL server met Windows authenticatie:

`mssqlclient.py -windows-auth {{domein}}/{{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Maak verbinding met SQL server-authenticatie:

`mssqlclient.py {{gebruikersnaam}}:{{wachtwoord}}@{{doel}}`

- Maak verbinding met pass-the-hash-authenticatie:

`mssqlclient.py {{domein}}/{{gebruikersnaam}}@{{doel}} -hashes {{LM_Hash}}:{{NT_Hash}}`

- Maak verbinding met Kerberos-authenticatie (geldige tickets vereist):

`mssqlclient.py -k {{domein}}/{{gebruikersnaam}}@{{doel}}`

- Voer een specifieke SQL-opdracht uit na verbinding:

`mssqlclient.py {{gebruikersnaam}}:{{wachtwoord}}@{{doel}} -query "{{SELECT user_name();}}"`

- Voer meerdere SQL-opdrachten vanuit een bestand uit:

`mssqlclient.py {{gebruikersnaam}}:{{wachtwoord}}@{{doel}} -file {{pad/naar/sql_bestand.sql}}`

- Maak verbinding met een specifieke database-instantie (standaard is `None`):

`mssqlclient.py {{gebruikersnaam}}:{{wachtwoord}}@{{doel}} -db {{database_naam}}`

- Geef SQL-query's weer voor uitvoering:

`mssqlclient.py {{gebruikersnaam}}:{{wachtwoord}}@{{doel}} -show`
