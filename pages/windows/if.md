# if

> Performs conditional processing in batch scripts.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/if>.

- Execute the specified commands if the condition is true:

`if {{condition}} {{commands}}`

- Execute the specified commands if the condition is false:

`if not {{condition}} {{commands}}`

- Execute the first specified commands if the condition is true otherwise execute the second specified commands:

`if {{condition}} ({{first_commands}}) else ({{second_commands}})`

- Check whether `%errorlevel%` is greater than or equal to the specified exit code:

`if errorlevel {{exit_code}} {{commands}}`

- Check whether two strings are equal:

`if {{string}} == {{string}} {{commands}}`

- Check whether two strings are equal without respecting letter case:

`if /i {{string}} == {{string}} {{commands}}`

- Check whether a file exist:

`if exist {{path/to/file}} {{commands}}`
