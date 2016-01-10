# sort

> Sort lines of text files.

- Sort a file in ascending order:

`sort {{filename}}`

- Sort a file in descending order:

`sort -r {{filename}}`

- Sort passwd file by the 3rd field:

`sort -t: -k 3n /etc/passwd`
