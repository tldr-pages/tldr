# isutf8

> Check whether text files contain valid UTF-8.
> More information: <https://joeyh.name/code/moreutils/>.

- Check whether the specified files contain valid UTF-8:

`isutf8 {{path/to/file1 path/to/file2 ...}}`

- Print errors using multiple lines:

`isutf8 --verbose {{path/to/file1 path/to/file2 ...}}`

- Do not print anything to `stdout`, indicate the result merely with the exit code:

`isutf8 --quiet {{path/to/file1 path/to/file2 ...}}`

- Only print the names of the files containing invalid UTF-8:

`isutf8 --list {{path/to/file1 path/to/file2 ...}}`

- Same as `--list` but inverted, i.e., only print the names of the files containing valid UTF-8:

`isutf8 --invert {{path/to/file1 path/to/file2 ...}}`
