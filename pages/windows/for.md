# for

> Conditionally perform a command several times.
> More information: <https://ss64.com/nt/for.html>.

- Iterate over range:

`for /l %I in ({{from}}, {{step}}, {{to}}) do {{command}}`

- Iterate over files:

`for %F in ({{file_set}}) do {{command}}`

- Iterate over directories:

`for /d %D in ({{folder_set}}) do {{command}}`
