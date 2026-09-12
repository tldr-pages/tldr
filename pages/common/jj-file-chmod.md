# jj file chmod

> Set or remove the executable bit for paths in a `jj` repository.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-chmod>.

- Make a file executable in the working copy:

`jj file chmod {{[x|executable]}} {{path/to/file}}`

- Make a file non-executable (normal) in the working copy:

`jj file chmod {{[n|normal]}} {{path/to/file}}`

- Make multiple files executable:

`jj file chmod {{[x|executable]}} {{path/to/file1 path/to/file2 ...}}`

- Make a file executable in a specific revision:

`jj file chmod {{[-r|--revision]}} {{revision}} {{[x|executable]}} {{path/to/file}}`
