# rpcinfo

> Realizează un apel RPC către un server RPC și raportează ce găsește.

- Afișați tabelul complet al tuturor serviciilor RPC înregistrate pe localhost:

`rpcinfo`

- Afișați tabelul concis al tuturor serviciilor RPC înregistrate pe localhost:

`rpcinfo -s {{localhost}}`

- Tabelul de afișare a statisticilor operațiilor rpcbind pe localhost:

`rpcinfo -m`

- Afișarea listei de intrări cu numele serviciului dat (mountd) și numărul de versiune (2) pe o partajare nfs la distanță:

`rpcinfo -l {{remote_nfs_server_ip}} {{mountd}} {{2}}`

- Ștergeți înregistrarea pentru versiunea 1 a serviciului mountd pentru toate transporturile:

`rpcinfo -d {{mountd}} {{1}}`
