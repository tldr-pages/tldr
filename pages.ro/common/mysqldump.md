# mysqldump

> Backup-uri de date MySQL.
> Vezi, de asemenea, `mysql` pentru restaurarea bazelor de date.
> Mai multe informaţii: <https://dev.mysql.com/doc/refman/en/mysqldump.html>

- Creați o copie de rezervă (utilizatorul va fi solicitat o parolă):

`mysqldump --user {{user}} --password {{database_name}} --result-file={{path/to/file.sql}}`

- Copierea de rezervă a unui tabel specific care redirecționează ieșirea către un fișier (utilizatorul va primi o parolă):

`mysqldump --user {{user}} --password {{database_name}} {{table_name}} > {{path/to/file.sql}}`

- Copierea de rezervă a tuturor bazelor de date care redirecționează ieșirea către un fișier (utilizatorul va primi o parolă):

`mysqldump --user {{user}} --password --all-databases > {{path/to/file.sql}}`

- Copierea de rezervă a tuturor bazelor de date dintr-o gazdă la distanță, redirecționarea ieșirii către un fișier (utilizatorul va fi solicitat o parolă):

`mysqldump --host={(ip_or_hostname)} --user {{user}} --password --all-databases > ({path/to/file.sql}}`
