# if

> Performs conditional processing in batch programs.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/if>.

- Check whether `%errorlevel%` is greater than or equal to the specified exit code:

`if errorlevel {{exit_code}} {{command}}`

- Check whether two strings are equal:

`if {{string}} == {{string}} {{command}}`

- Check whether two strings are equal without respecting letter case:

`if /i {{string}} == {{string}} {{command}}`

- Check whether a file exist:

`if exist {{path/to/file}} {{command}}`

- Check whether a condition is false:

`if not {{condition}} {{command}}`
