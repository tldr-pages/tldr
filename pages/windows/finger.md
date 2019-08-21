# finger

> Return information about one or more users on a specified system.
> The remote system must be running the Finger service.
> More information: <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/finger>.

- Display information about a specific user:

`finger {{user}}@{{host}}`

- Display information about all users on the specified host:

`finger @{{host}}`

- Display information in a longer format:

`finger {{user}}@{{host}} -l`

- Display help information:

`finger /?`
