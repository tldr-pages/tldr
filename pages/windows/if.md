# if

> Performs conditional processing in batch programs.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/if>.

- Execute the specified command if the condition is true:

`if {{condition}} {{command}}`

- Execute the specified command if the condition is false:

`if not {{condition}} {{command}}`

- Execute the first specified command if the condition is true otherwise execute the second specified command:

`if {{condition}} ({{first_command}}) else ({{second_command}})`

- Check whether `%errorlevel%` is greater than or equal to the specified exit code:

`if errorlevel {{exit_code}} {{command}}`

- Check whether two strings are equal:

`if {{string}} == {{string}} {{command}}`

- Check whether two strings are equal without respecting letter case:

`if /i {{string}} == {{string}} {{command}}`

- Check whether a file exist:

`if exist {{path/to/file}} {{command}}`
