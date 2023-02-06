# kill

> Jelzést küld egy folyamatnak, általában a folyamat leállításával kapcsolatban. A SIGKILL és SIGSTOP kivételével minden jelet a folyamat elfoghat, hogy tiszta kilépést hajtson végre. További információ: <https://manned.org/kill>.

- Egy program befejezése az alapértelmezett SIGTERM (terminate) jel segítségével:

`kill {{process_id}}`

- A rendelkezésre álló jelnevek listája (a `SIG` előtag nélkül használandó):

`kill -l`

- Háttérmunkák befejezése:

`kill %{{job_id}}`

- Egy program befejezése a SIGHUP (leállás) jel használatával. Sok démon a program befejezése helyett újratöltődik:

`kill -{{1|HUP}} {{process_id}}`

- Program befejezése a SIGINT (megszakítás) jel használatával. Ezt általában a felhasználó kezdeményezi a `Ctrl + C` megnyomásával:

`kill -{{2|INT}} {{process_id}}`

- Jelezzük az operációs rendszernek, hogy azonnal fejezze be a programot (amely nem kap esélyt a jel rögzítésére):

`kill -{{9|KILL}} {{process_id}}`

- Jelezzük az operációs rendszernek, hogy szüneteltessen egy programot, amíg a SIGCONT ("continue") jelet nem kapjuk:

`kill -{{17|STOP}} {{process_id}}`

- `SIGUSR1` jelet küldeni az adott GID (group id) jelzéssel rendelkező összes folyamatnak:

`kill -{{SIGUSR1}} -{{group_id}}`
