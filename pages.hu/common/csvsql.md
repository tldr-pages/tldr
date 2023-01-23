# csvsql

> SQL utasítások generálása egy CSV fájlhoz, vagy ezen utasítások közvetlen végrehajtása egy adatbázisban. A csvkit része. További információ: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

- Generálja a `CREATE TABLE` SQL utasítást egy CSV fájlhoz:

`csvsql {{path/to/data.csv}}`

- Importáljon egy CSV-fájlt egy SQL-adatbázisba:

`csvsql --insert --db "{{mysql://user:password@host/database}}" {{data.csv}}`

- SQL-lekérdezés futtatása egy CSV-fájlon:

`csvsql --query "{{select * from 'data'}}" {{data.csv}}`
