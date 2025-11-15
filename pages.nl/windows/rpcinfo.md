# rpcinfo

> Toon programma's via RPC op externe computers.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- Toon alle programma's geregistreerd op de lokale computer:

`rpcinfo`

- Toon alle programma's geregistreerd op een externe computer:

`rpcinfo /p {{computer_naam}}`

- Roep een specifiek programma aan op een externe computer via TCP:

`rpcinfo /t {{computer_naam}} {{programma_naam}}`

- Roep een specifiek programma aan op een externe computer via UDP:

`rpcinfo /u {{computer_naam}} {{programma_naam}}`
