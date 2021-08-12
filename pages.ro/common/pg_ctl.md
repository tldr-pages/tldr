# pg_ctl

> Utilitar pentru controlul unui server PostgreSQL şi al unui cluster de baze de date.
> Mai multe informaţii: <https://www.postgresql.org/docs/current/app-pg-ctl.html>

- Iniţializaţi un nou cluster de baze de date PostgreSQL:

`pg_ctl -D {{data_directory}} init`

- Porniţi un server PostgreSQL:

`pg_ctl -D {{data_directory}} start`

- Opriţi un server PostgreSQL:

`pg_ctl -D {{data_directory}} stop`

- Reporniţi un server PostgreSQL:

`pg_ctl -D {{data_directory}} restart`

- Reîncarcă configuraţia serverului PostgreSQL:

`pg_ctl -D {{data_directory}} reload`
