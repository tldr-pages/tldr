# sort

> Sort lines of text files.

- Sort a file in ascending order:

`sort {{filename}}`

- Sort a file in descending order:

`sort -r {{filename}}`

- Sort a file using numeric rather than alphabetic order:

`sort -n {{filename}}`

- Sort the passwd file by the 3rd field, numerically:

`sort -t: -k 3n /etc/passwd`

- Sort a file preserving only unique lines:

`sort -u {{filename}}`
