# csvsql

> Generați declarații SQL pentru un fișier CSV sau executați aceste declarații direct pe o bază de date.
> Inclus în csvkit.
> Mai multe informaţii: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>

- Generați o instrucțiune SQL `CREATE TABLE' pentru un fișier CSV:

`csvsql {{path/to/data.csv}}`

- Importați un fișier CSV într-o bază de date SQL:

`csvsql --insert --db "{{mysql://user:password@host/database}}" {{data.csv}}`

- Rulați o interogare SQL pe un fișier CSV:

`csvsql --query "{{select * from 'data'}}" {{data.csv}}`
