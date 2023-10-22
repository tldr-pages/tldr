# for

> Conditionally execute a command several times.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- Execute given commands for the specified set:

`for %{{variable}} in ({{item_a item_b item_c}}) do ({{echo Loop is executed}})`

- Iterate over a given range of numbers:

`for /l %{{variable}} in ({{from}}, {{step}}, {{to}}) do ({{echo Loop is executed}})`

- Iterate over a given list of files:

`for %{{variable}} in ({{path\to\file1.ext path\to\file2.ext ...}}) do ({{echo Loop is executed}})`

- Iterate over a given list of directories:

`for /d %{{variable}} in ({{path\to\directory1.ext path\to\directory2.ext ...}}) do ({{echo Loop is executed}})`

- Perform a given command in every directory:

`for /d %{{variable}} in (*) do (if exist %{{variable}} {{echo Loop is executed}})`
