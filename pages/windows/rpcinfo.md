# rpcinfo

> List programs via RPC on remote computers.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- List all programs registered on the local computer:

`rpcinfo`

- List all programs registered on a remote computer:

`rpcinfo /p {{computer_name}}`

- Call a specific program on a remote computer using TCP:

`rpcinfo /t {{computer_name}} {{program_name}}`

- Call a specific program on a remote computer using UDP:

`rpcinfo /u {{computer_name}} {{program_name}}`
