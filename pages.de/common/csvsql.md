# csvsql

> Generiert SQL-Anweisungen für eine CSV-Datei oder führt diese Anweisungen direkt in einer Datenbank aus.
> In csvkit enthalten.
> Mehr Informationen: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

- Generiert eine `CREATE TABLE`-SQL-Anweisung für eine CSV-Datei:

`csvsql {{pfad/zur/daten.csv}}`

- Importiert eine CSV-Datei in eine SQL-Datenbank:

`csvsql --insert --db "{{mysql://benutzer:passwort@host/datenbank}}" {{daten.csv}}`

- Führt eine SQL-Abfrage auf einer CSV-Datei aus:

`csvsql --query "{{select * from 'daten'}}" {{daten.csv}}`
