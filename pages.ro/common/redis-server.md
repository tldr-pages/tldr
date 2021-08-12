# redis-server

> Baza de date persistentă cheie-valoare.
> Mai multe informaţii: <https://redis.io>

- Porniți serverul Redis, utilizând portul implicit (6379), și scrieți jurnalele la stdout:

`redis-server`

- Porniți serverul Redis, utilizând portul implicit, ca proces de fundal:

`redis-server --daemonize yes`

- Porniți serverul Redis, folosind portul specificat, ca proces de fundal:

`redis-server --port {{port}} --daemonize yes`

- Porniți serverul Redis cu un fișier de configurare personalizat:

`redis-server {{path/to/redis.conf}}`

- Porniți serverul Redis cu logare detaliată:

`redis-server --loglevel {{warning|notice|verbose|debug}}`
