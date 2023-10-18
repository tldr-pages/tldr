# runlim

> A tool for sampling and limiting time and memory usage of a program and its child processes using the proc file system on Linux.
> More information: <http://fmv.jku.at/runlim>.

- Print the time and memory usage of a command:

`runlim {{command}} {{command_arguments}}`

- Log statistics to a file instead of `stdout`:

`runlim --output-file={{path/to/file}} {{command}} {{command_arguments}}`

- Limit time to an upper bound (in seconds):

`runlim --time-limit={{number}} {{command}} {{command_arguments}}`

- Limit real-time to an upper bound (in seconds):

`runlim --real-time-limit={{number}} {{command}} {{command_arguments}}`

- Limit space to an upper bound (in MB):

`runlim --space-limit={{number}} {{command}} {{command_arguments}}`
