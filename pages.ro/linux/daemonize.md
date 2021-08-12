# daemonize

> Rulați o comandă (care nu se daemonizează) ca un daemon Unix.
> Mai multe informaţii: <http://software.clapper.org/daemonize/>

- Rulează o comandă ca un daemon:

`daemonize {{command}} {{command_arguments}}`

- Scrieți pid în fișierul specificat:

`daemonize -p {{path/to/pidfile}} {{command}} {{command_arguments}}`

- Utilizați un fișier de blocare pentru a vă asigura că numai o singură instanță rulează la un moment dat:

`daemonize -l {{path/to/lockfile}} {{command}} {{command_arguments}}`

- Utilizați contul de utilizator specificat:

`sudo daemonize -u {{user}} {{command}} {{command_arguments}}`
