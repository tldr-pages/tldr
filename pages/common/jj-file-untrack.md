# jj file untrack

> Stop tracking specified paths in the working copy of a `jj` repository.
> The paths must already be ignored (e.g. via `.gitignore`).
> See also: `jj file track`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-file-untrack>.

- Stop tracking an ignored file or directory:

`jj file untrack {{path/to/file_or_directory}}`

- Stop tracking multiple ignored paths:

`jj file untrack {{path/to/file1 path/to/directory2 ...}}`
