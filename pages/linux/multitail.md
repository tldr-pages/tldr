# multitail

> MultiTail -  allows you to monitor logfiles and command output in multiple windows in a terminal, colorize, filter and merge.

- Options

`-i file  - Select a file to monitor. You can have multiple -i file parameters. You only need to add -i file in front of a filename if the filename starts with a dash ('-').`

`-I file - Same as -i file but add the output to the previous window (so the output is merged).`

`-l command - Command to execute in a window. Parameter is the command. Do not forget to use "'s if the external command needs parameter! (e.g. -l "ping host").`

`-L command - Same as -l but add the output to the previous window (so the output is merged).`

`-n number_of_lines - Number of lines to tail initially. The default depends on the size of the terminal-window.`
