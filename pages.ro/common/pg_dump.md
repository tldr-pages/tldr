# pg_dump

> Extrageţi o bază de date PostgreSQL într-un fişier script sau alt fişier de arhivă.
> Mai multe informaţii: <https://www.postgresql.org/docs/current/app-pgdump.html>

- Dump baza de date într-un fișier SQL-script:

`pg_dump {{db_name}} > {{output_file.sql}}`

- La fel ca mai sus, personalizați numele de utilizator:

`pg_dump -U {{username}} {{db_name}} > {{output_file.sql}}`

- La fel ca mai sus, personalizați gazdă și port:

`pg_dump -h {{host}} -p {{port}} {{db_name}} > {{output_file.sql}}`

- Dump o bază de date într-un fișier de arhivă de format particularizat:

`pg_dump -Fc {{db_name}} > {{output_file.dump}}`

- Dump numai datele bazei de date într-un fișier SQL-script:

`pg_dump -a {{db_name}} > {{path/to/output_file.sql}}`

- Dump numai schemă (definiții de date) într-un fișier SQL-script:

`pg_dump -s {{db_name}} > {{path/to/output_file.sql}}`
