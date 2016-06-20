# unexpand

> Convert spaces to tabs.

- Convert blanks in each FILE to tabs, writing to standard output:

`unexpand {{FILE}}`

- Convert blanks to tabs, reading from standard output:

`unexpand`

- Convert all blanks, instead of just initial blanks:

`unexpand -a {{FILE}}`

- Convert only leading sequences of blanks (overrides -a):

`unexpand --first-only {{FILE}}`

- Have tabs NUMBER characters apart, not 8 (enables -a):

`unexpand -t {{NUMBER}} {{FILE}}`
