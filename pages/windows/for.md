# for

> Conditionally perform a command several times.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/for>.

- Iterate over range:

`for /l %I in ({{from}}, {{step}}, {{to}}) do {{command}}`

- Iterate over files:

`for %F in ({{file_set}}) do {{command}}`

- Iterate over directories:

`for /d %D in ({{folder_set}}) do {{command}}`
