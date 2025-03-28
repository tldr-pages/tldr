# lsns

> List information about all namespaces or about the specified namespace.
> More information: <https://manned.org/lsns>.

- List all namespaces:

`lsns`

- List namespaces in JSON format:

`lsns {{[-J|--json]}}`

- List namespaces associated with the specified process:

`lsns {{[-p|--task]}} {{pid}}`

- List the specified type of namespaces only:

`lsns {{[-t|--type]}} {{mnt|net|ipc|user|pid|uts|cgroup|time}}`

- List namespaces, only showing the namespace ID, type, PID, and command:

`lsns {{[-o|--output]}} {{NS,TYPE,PID,COMMAND}}`
