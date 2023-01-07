# for

> Conditionally execute a command several times.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- Execute given commands for the specified set:

`for %{{variable}} in ({{item_a item_b item_c}}) do ({{echo Loop is executed}})`

- Iterate over a given range of numbers:

`for /l %{{variable}} in ({{from}}, {{step}}, {{to}}) do ({{echo Loop is executed}})`

- Iterate over a given list of files:

`for %{{variable}} in ({{file_a.ext file_b.ext file_c.ext}}) do ({{echo Loop is executed}})`

- Iterate over a given list of directories:

`for /d %{{variable}} in ({{directory_a/ directory_b/ directory_c/}}) do ({{echo Loop is executed}})`

- Perform a given command in every directory:

`for /d %{{variable}} in (*) do (if exist %{{variable}} {{echo Loop is executed}})`
