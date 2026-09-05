# jj file track

> Start tracking specified paths in the working copy of a `jj` repository.
> See also: `jj file untrack`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-track>.

- Track all untracked files in the working copy:

`jj file track`

- Track a specific file or directory:

`jj file track {{path/to/file_or_directory}}`

- Track multiple paths:

`jj file track {{path/to/file1 path/to/directory2 ...}}`

- Track paths even if they are ignored or exceed the maximum file size:

`jj file track --include-ignored {{path/to/file_or_directory}}`
