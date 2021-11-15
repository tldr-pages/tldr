# for

> Performs conditional processing in batch programs.
> More information: <https://ss64.com/nt/for.html>.

- Check whether %errorlevel% is greater than or equal to:

`if errorlevel {{exit_code}} {{command}}`

- Check whether two strings are equal:

`if {{string}} == {{string}} {{command}}`

- Check whether two strings are equal without respecting letter case:

`if /i {{string}} == {{string}} {{command}}`

- Check whether file exist:

`if exist {{path/to/file}} {{command}}`

- Check whether negated condition is true:

`if not {{condition}} {{command}}`
