# rename

> Rename a file or group of files with a regular expression.
> Get help or version: rename --help|--version.
> More information: <https://man7.org/linux/man-pages/man1/rename.1.html>.

- Replace `from` with `to` in the filenames of the specified files:

`rename 's/{{from}}/{{to}}/' {{*.txt}}`
