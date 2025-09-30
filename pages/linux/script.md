# script

> Record all terminal output to a typescript file.
> More information: <https://manned.org/script>.

- Record a new session to a file named `typescript` in the current directory:

`script`

- Stop recording:

`exit`

- Record a new session to a custom filepath:

`script {{path/to/session.out}}`

- Append to an existing file:

`script {{[-a|--append]}} {{logfile.log}}`

- Record timing information (data is outputted to `stderr`):

`script {{[-t|--timing]}} 2> {{path/to/timing_file}}`

- Write out data as soon as it happens:

`script {{[-f|--flush]}} {{path/to/file}}`

- Execute quietly without start and done messages:

`script {{[-q|--quiet]}} {{logfile.log}}`

- Display help:

`script {{[-h|--help]}}`
