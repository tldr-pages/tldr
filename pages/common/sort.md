# sort

> Sort lines of text files.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

- Sort a file in ascending order:

`sort {{path/to/file}}`

- Sort a file in descending order:

`sort -r {{path/to/file}}`

- Sort a file in case-insensitive way:

`sort --ignore-case {{path/to/file}}`

- Sort a file using numeric rather than alphabetic order:

`sort -n {{path/to/file}}`

- Sort the passwd file by the 3rd field, numerically:

`sort -t: -k 3n /etc/passwd`

- Sort a file preserving only unique lines:

`sort -u {{path/to/file}}`

- Sort human-readable numbers (in this case the 5th field of `ls -lh`):

`ls -lh | sort -h -k 5`

- Sort numbers with exponents:

`sort --general-numeric-sort {{path/to/file}}`
