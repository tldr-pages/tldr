# mysql

> Instrumentul de linie de comandă MySQL.
> Mai multe informaţii: <https://www.mysql.com/>

- Conectarea la o bază de date:

`mysql {{database_name}}`

- Conectarea la o bază de date, utilizatorul va fi solicitat pentru o parolă:

`mysql -u {{user}} --password {{database_name}}`

- Conectați-vă la o bază de date pe o altă gazdă:

`mysql -h {{database_host}} {{database_name}}`

- Conectarea la o bază de date printr-un soclu Unix:

`mysql --socket {{path/to/socket.sock}}`

- Execută declarații SQL într-un fișier script (fișier batch):

`mysql -e "source {{filename.sql}}" {{database_name}}`

- Restaurați o bază de date dintr-o copie de rezervă creată cu `mysqldump` (utilizatorul va fi solicitat pentru o parolă):

`mysql --user {{user}} --password {{database_name}} < {{path/to/backup.sql}}`

- Restaurați toate bazele de date dintr-o copie de rezervă (utilizatorul va fi solicitat o parolă):

`mysql --user {{user}} --password < {{path/to/backup.sql}}`
