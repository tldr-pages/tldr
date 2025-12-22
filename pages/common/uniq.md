# uniq

> Output the unique lines from a input or file.
> Since it does not detect repeated lines unless they are adjacent, we need to sort them first.
> See also: `sort`.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html>.

- Display each line once:

`sort {{path/to/file}} | uniq`

- Display only unique lines:

`sort {{path/to/file}} | uniq {{[-u|--unique]}}`

- Display only duplicate lines:

`sort {{path/to/file}} | uniq {{[-d|--repeated]}}`

- Display number of occurrences of each line along with that line:

`sort {{path/to/file}} | uniq {{[-c|--count]}}`

- Display number of occurrences of each line, sorted by the most frequent:

`sort {{path/to/file}} | uniq {{[-c|--count]}} | sort {{[-nr|--numeric-sort --reverse]}}`

- Compare only the first 5 characters on each line for uniqueness:

`sort {{path/to/file}} | uniq {{[-w|--check-chars]}} 5`

- Compare text after the first 5 character on each line for uniqueness:

`sort {{path/to/file}} | uniq {{[-s|--skip-chars]}} 5`
