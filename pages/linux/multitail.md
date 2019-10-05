# multitail

> MultiTail -  allows you to monitor logfiles and command output in multiple windows in a terminal, colorize, filter and merge.

- Select a file to monitor:

`multitail -i file`

- Monitor file and output to the previous window (so the output is merged):

`multitail -I file`

- Command to execute in a window. Parameter is the command. Do not forget to use "'s if the external command needs parameter! (e.g. -l "ping host"):

`multitail -l command`

- Same as -l but add the output to the previous window (so the output is merged):

`multitail -L command`

- Number of lines to tail initially. The default depends on the size of the terminal-window:

`multitail -n number_of_lines`
