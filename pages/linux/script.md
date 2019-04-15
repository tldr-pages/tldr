# script

> Record all terminal output to file.

- Record user's session to a file named "typescript" in current directory:

`script`

- Record user's session to a file named "session.out":

`script session.out`

- Record user's session, appending to existing "session.out":

`script -a session.out`

- Record user's session to a file for replay later:

`script -t 2> {{timingfile}}`
