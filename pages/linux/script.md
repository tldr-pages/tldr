# script

> Record all terminal output to file.
> More information: <https://manned.org/script>.

- Record a new session to a file named `typescript` in the current directory:

`script`

- Record a new session to a custom filepath:

`script {{path/to/session.out}}`

- Record a new session, appending to an existing file:

`script -a {{path/to/session.out}}`

- Record timing information (data is outputted to `stderr`):

`script -t 2> {{path/to/timing_file}}`

- Write out data as soon as it happens:

`script -f {{path/to/file}}`
