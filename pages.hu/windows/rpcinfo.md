# rpcinfo

> Programok listázása RPC-n keresztül távoli számítógépeken. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- A helyi számítógépen regisztrált összes program listázása:

`rpcinfo`

- Távoli számítógépen regisztrált összes program listázása:

`rpcinfo /p {{computer_name}}`

- Egy adott program hívása egy távoli számítógépen TCP segítségével:

`rpcinfo /t {{computer_name}} {{program_name}}`

- Egy adott program hívása egy távoli számítógépen UDP segítségével:

`rpcinfo /u {{computer_name}} {{program_name}}`
