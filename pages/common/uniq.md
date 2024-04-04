# uniq

> Output the unique lines from a input or file.
> Since it does not detect repeated lines unless they are adjacent, we need to sort them first.
> More information: <https://www.gnu.org/software/coreutils/uniq>.

- Display each line once:

`sort {{path/to/file}} | uniq`

- Display only unique lines:

`sort {{path/to/file}} | uniq -u`

- Display only duplicate lines:

`sort {{path/to/file}} | uniq -d`

- Display number of occurrences of each line along with that line:

`sort {{path/to/file}} | uniq -c`

- Display number of occurrences of each line, sorted by the most frequent:

`sort {{path/to/file}} | uniq -c | sort -nr`
