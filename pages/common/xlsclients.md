# xlsclients

> List client applications running on an X11 display.
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

`xlsclients -display :{{display_number}}`

- List clients on remote host's display:

`xlsclients -display {{remote_host}}:0`

- Display version:

`xlsclients -version`
