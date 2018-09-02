# join

> Join lines of two sorted files on a common field.

- Join two files on the first (default) field:

`join {{file1}} {{file2}}`

- Join field3 of file1 with field1 of file2:

`join -1 3 -2 1 {{file1}} {{file2}}`

- Produce a line for each unpairable line for file1:

`join -a 1 {{file1}} {{file2}}`
