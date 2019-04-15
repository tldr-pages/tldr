# script

> Record all terminal output to file.

- Record a new session to a file named `typescript` in the current directory:

`script`

- Record a new session to custom filepath:

`script {{path/to/session.out}}`

- Record a new session, appending to an existing file:

`script -a session.out`

- Record timing information (data is outputted to the standard error):

`script -t 2> {{timingfile}}`
