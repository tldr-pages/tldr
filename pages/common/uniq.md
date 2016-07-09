# uniq

> Output the unique lines from the given input or file.

- Display each line once:

`uniq {{file}}`

- Display only unique lines:

`uniq -u {{file}}`

- Display only duplicate lines:

`uniq -d {{file}}`

- Display number of occurences of each line along with that line:

`uniq -c {{file}}`

- Display number of occurences of each line, sorted by the most frequent:

`uniq -c {{file}} | sort -nr`
