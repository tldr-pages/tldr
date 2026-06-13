# csvsql

> Generiere SQL-Anweisungen für eine CSV-Datei oder führe diese Anweisungen direkt in einer Datenbank aus.
> Teil von csvkit.
> Weitere Informationen: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

- Generiere eine `CREATE TABLE`-SQL-Anweisung für eine CSV-Datei:

`csvsql {{pfad/zu/datei.csv}}`

- Importiere eine CSV-Datei in eine SQL-Datenbank:

`csvsql --insert --db "{{mysql://benutzer:passwort@host/datenbank}}" {{pfad/zu/datei.csv}}`

- Führe eine SQL-Abfrage auf einer CSV-Datei aus:

`csvsql --query "{{select * from 'datei'}}" {{datei.csv}}`
