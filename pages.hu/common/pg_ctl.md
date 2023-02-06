# pg_ctl

> PostgreSQL szerver és adatbázis-fürt vezérlésére szolgáló segédprogram. További információ: <https://www.postgresql.org/docs/current/app-pg-ctl.html>.

- Új PostgreSQL adatbázis-fürt inicializálása:

`pg_ctl -D {{data_directory}} init`

- Indítson el egy PostgreSQL kiszolgálót:

`pg_ctl -D {{data_directory}} start`

- Egy PostgreSQL kiszolgáló leállítása:

`pg_ctl -D {{data_directory}} stop`

- Egy PostgreSQL kiszolgáló újraindítása:

`pg_ctl -D {{data_directory}} restart`

- A PostgreSQL kiszolgáló konfigurációjának újratöltése:

`pg_ctl -D {{data_directory}} reload`
