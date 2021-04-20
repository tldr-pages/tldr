# sort

> Sort lines of text files.
> More information: <https://www.gnu.org/software/coreutils/sort>.

- Sort a file in ascending order:

`sort {{path/to/file}}`

- Sort a file in descending order:

`sort --reverse {{path/to/file}}`

- Sort a file in case-insensitive way:

`sort --ignore-case {{path/to/file}}`

- Sort a file using numeric rather than alphabetic order:

`sort --numeric-sort {{path/to/file}}`

- Sort `/etc/passwd` by the 3rd field of each line numerically, using ":" as a field separator:

`sort --field-separator={{:}} --key={{3n}} {{/etc/passwd}}`

- Sort a file preserving only unique lines:

`sort --unique {{path/to/file}}`

- Sort a file, printing the output to the specified output file (can be used to sort a file in-place):

`sort --output={{path/to/file}} {{path/to/file}}`

- Sort numbers with exponents:

`sort --general-numeric-sort {{path/to/file}}`
