# lsns

> Az összes névtérre vagy a megadott névtérre vonatkozó információk listázása. További információ: <https://man7.org/linux/man-pages/man8/lsns.8.html>.

- Az összes névtér listázása:

`lsns`

- Névterek listázása JSON formátumban:

`lsns --json`

- List namespaces associated with {{pid}}:

`lsns --task {{pid}}`

- Csak a megadott típusú névterek listázása:

`lsns --type <mnt|net|ipc|user|pid|uts|cgroup|time>`

- Névterek listázása, csak a névtér azonosítójának, típusának, PID-jének és parancsának feltüntetésével:

`lsns --output NS,TYPE,PID,COMMAND`
