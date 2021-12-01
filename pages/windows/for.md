# for

> Conditionally perform a command several times.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/for>.

- Execute the specified commands for the specified set:

`for %{{variable}} in ({{set}}) do (echo Variable {{variable}} is %{{variable}} now)`

- Iterate over range:

`for /l %{{variable}} in ({{from}}, {{step}}, {{to}}) do (echo Variable {{variable}} is %{{variable}} now)`

- Iterate over files:

`for %{{variable}} in ({{file_set}}) do (echo Variable {{variable}} is %{{variable}} now)`

- Iterate over directories:

`for /d %{{variable}} in ({{folder_set}}) do (echo Variable {{variable}} is %{{variable}} now)`
