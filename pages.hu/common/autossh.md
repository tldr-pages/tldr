# autossh

> SSH-kapcsolatok futtatása, felügyelete és újraindítása. Automatikus újracsatlakozás a porttovábbítási alagutak fenntartása érdekében. Elfogadja az összes `ssh` zászlót. További információ: <https://www.harding.motd.ca/autossh>.

- SSH-munkamenet indítása, újraindítás, ha egy felügyeleti port nem küld vissza adatokat:

`autossh -M {{monitor_port}} "{{ssh_command}}"`

- Helyi port továbbítása távoli portra, újraindítás, ha szükséges:

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- A `autossh` elágazása a háttérbe a `ssh` végrehajtása előtt, és ne nyisson távoli héjat:

`autossh -f -M {{monitor_port}} -N "{{ssh_command}}"`

- Futtassa a háttérben, felügyeleti port nélkül, és helyette 10 másodpercenként küldjön SSH keep-alive csomagokat a hiba észlelésére:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_command}}"`

- Futtassa a háttérben, felügyeleti port és távoli héj nélkül, és lépjen ki, ha a port továbbítása sikertelen:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Futtatás a háttérben, a `autossh` debug kimenet és a `ssh` verbose kimenet naplózása fájlokban:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{path/to/autossh_log_file.log}} autossh -f -M {{monitor_port}} -v -E {{path/to/ssh_log_file.log}} {{ssh_command}}`
