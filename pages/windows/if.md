# if

> Performs conditional processing in batch scripts.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/if>.

- Execute the specified commands if the condition is true:

`if {{condition}} ({{echo Condition is true}})`

- Execute the specified commands if the condition is false:

`if not {{condition}} ({{echo Condition is true}})`

- Execute the first specified commands if the condition is true otherwise execute the second specified commands:

`if {{condition}} ({{echo Condition is true}}) else ({{echo Condition is false}})`

- Check whether `%errorlevel%` is greater than or equal to the specified exit code:

`if errorlevel {{exit_code}} ({{echo Condition is true}})`

- Check whether two strings are equal:

`if %{{variable}}% == {{string}} ({{echo Condition is true}})`

- Check whether two strings are equal without respecting letter case:

`if /i %{{variable}}% == {{string}} ({{echo Condition is true}})`

- Check whether a file exist:

`if exist {{path/to/file}} ({{echo Condition is true}})`
