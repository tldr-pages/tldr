# for

> Conditionally execute a command several times.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/for>.

- Execute the specified commands for the specified set:

`for %{{variable}} in ({{item_a item_b item_c}}) do ({{echo Loop is executed}})`

- Iterate over range:

`for /l %{{variable}} in ({{from}}, {{step}}, {{to}}) do ({{echo Loop is executed}})`

- Iterate over files:

`for %{{variable}} in ({{file_a.ext file_b.ext file_c.ext}}) do ({{echo Loop is executed}})`

- Iterate over directories:

`for /d %{{variable}} in ({{directory_a/ directory_b/ directory_c/}}) do ({{echo Loop is executed}})`

- Perform a command in every directory:

`for /d %{{variable}} in (*) do (if exist %{{variable}} {{echo Loop is executed}})`
