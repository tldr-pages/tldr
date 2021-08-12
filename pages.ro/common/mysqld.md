# mysqld

> Porniți serverul de baze de date MySQL.
> Mai multe informaţii: <https://dev.mysql.com/doc/refman/en/mysqld.html>

- Porniți serverul de baze de date MySQL:

`mysqld`

- Porniți serverul, tipărirea mesajelor de eroare la consola:

`mysqld --console`

- Porniți serverul, salvând ieșirea în jurnal într-un fișier jurnal personalizat:

`mysqld --log={{path/to/file.log}}`

- Imprimați argumentele implicite și valorile acestora și ieșiți:

`mysqld --print-defaults`

- Porniți serverul, citirea argumentelor și valorilor dintr-un fișier:

`mysqld --defaults-file={{path/to/file}}`

- Porniți serverul și ascultați pe un port personalizat:

`mysqld --port={{port}}`

- Afișați toate opțiunile de ajutor și ieșiți:

`mysqld --verbose --help`
