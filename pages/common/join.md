# join

> Join lines of two sorted files on a common field.
> More information: <https://www.gnu.org/software/coreutils/join>.

- Join two files on the first (default) field:

`join {{file1}} {{file2}}`

- Join two files using a comma (instead of a space) as the field separator:

`join -t {{','}} {{file1}} {{file2}}`

- Join field3 of file1 with field1 of file2:

`join -1 {{3}} -2 {{1}} {{file1}} {{file2}}`

- Produce a line for each unpairable line for file1:

`join -a {{1}} {{file1}} {{file2}}`

- Join a file from `stdin`:

`cat {{path/to/file1}} | join - {{path/to/file2}}`
