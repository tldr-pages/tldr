# runlim

> A tool for sampling and limiting time and memory usage of a program and its child processes using the proc file system on Linux.
> More information: <http://fmv.jku.at/runlim>.

- Print the time and memory usage of a command:

`runlim {{command}}`

- Create output file for logging:

`runlim -o {{file name}} {{command}}`

- Limit time to an upper bound (in seconds):

`runlim -t {{number}} {{command}}`

- Limit real-time to an upper bound (in seconds):

`runlim -r {{number}} {{command}}`

- Limit space to an upper bound (in MB):

`runlim -s {{number}} {{command}}`
