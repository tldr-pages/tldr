# pg_restore

> Restaurați o bază de date PostgreSQL dintr-un fișier de arhivă creat de pg_dump.
> Mai multe informaţii: <https://www.postgresql.org/docs/current/app-pgrestore.html>

- Restaurarea unei arhive într-o bază de date existentă:

`pg_restore -d {{db_name}} {{archive_file.dump}}`

- La fel ca mai sus, personalizați numele de utilizator:

`pg_restore -U {{username}} -d {{db_name}} {{archive_file.dump}}`

- La fel ca mai sus, personalizați gazdă și port:

`pg_restore -h {{host}} -p {{port}} -d {{db_name}} {{archive_file.dump}}`

- Lista obiectelor bazei de date incluse în arhivă:

`pg_restore --list {{archive_file.dump}}`

- Curățați obiectele bazei de date înainte de crearea lor:

`pg_restore --clean -d {{db_name}} {{archive_file.dump}}`

- Utilizați mai multe locuri de muncă pentru a face restaurarea:

`pg_restore -j {{2}} -d {{db_name}} {{archive_file.dump}}`
