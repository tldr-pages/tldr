# xlsclients

> List client applications running on an X11 display.
> Useful for capturing the current graphical session state or debugging.
> More information: <https://manned.org/xlsclients>.

- List clients on the default display:

`xlsclients`

- List clients on all screens:

`xlsclients -a`

- List clients with detailed information:

`xlsclients -l`

- Limit the command output length per client to a specific number of characters:

`xlsclients -m {{max_command_length}}`

- Specify a particular display to inspect:

`xlsclients -display {{hostname}}:{{display_number}}`

- Show the version of `xlsclients`:

`xlsclients -version`
