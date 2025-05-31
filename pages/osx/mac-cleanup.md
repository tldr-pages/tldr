# mac-cleanup

> A modern macOS cleanup tool to remove caches and junk.
> More information: <https://github.com/mac-cleanup/mac-cleanup-py>.

- Start the cleanup process:

`mac-cleanup`

- Open the module configuration screen:

`mac-cleanup {{[-c|--configure]}}`

- Perform a dry-run, showing what will be removed without actually deleting it:

`mac-cleanup {{[-n|--dry-run]}}`

- Specify the directory with custom cleanup path:

`mac-cleanup {{[-p|--custom-path]}} {{path/to/directory}}`

- Automatically acknowledge all warnings and continue with force:

`mac-cleanup {{[-f|--force]}}`
