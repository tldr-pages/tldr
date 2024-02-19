# diffstat

> Create a histogram from the output of the `diff` command.
> More information: <https://manned.org/diffstat>.

- Display changes in a histogram:

`diff {{path/to/file1}} {{path/to/file2}} | diffstat`

- Display inserted, deleted and modified changes as a table:

`diff {{path/to/file1}} {{path/to/file2}} | diffstat -t`
