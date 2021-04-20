# unexpand

> Convert spaces to tabs.
> More information: <https://www.gnu.org/software/coreutils/unexpand>.

- Convert blanks in each file to tabs, writing to standard output:

`unexpand {{file}}`

- Convert blanks to tabs, reading from standard output:

`unexpand`

- Convert all blanks, instead of just initial blanks:

`unexpand -a {{file}}`

- Convert only leading sequences of blanks (overrides -a):

`unexpand --first-only {{file}}`

- Have tabs a certain number of characters apart, not 8 (enables -a):

`unexpand -t {{number}} {{file}}`
