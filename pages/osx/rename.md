# rename

> Rename a file or group of files with a regex.

- Replace from.txt -> to.txt:

`rename 's/{{from}}/{{to}}/' {{*.txt}}`

- Replace all filename spaces with underscores for all files in the current directory:

`rename 's/ /_/g' *`
