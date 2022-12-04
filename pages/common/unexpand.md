# unexpand

> Convert spaces to tabs.
> More information: <https://www.gnu.org/software/coreutils/unexpand>.

- Convert blanks in each file to tabs, writing to standard output:

`unexpand {{path/to/file}}`

- Convert blanks to tabs, reading from standard output:

`unexpand`

- Convert all blanks, instead of just initial blanks:

`unexpand -a {{path/to/file}}`

- Convert only leading sequences of blanks (overrides -a):

`unexpand --first-only {{path/to/file}}`

- Have tabs a certain number of characters apart, not 8 (enables -a):

`unexpand -t {{number}} {{path/to/file}}`
