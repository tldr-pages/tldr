# gup

> Update binaries installed by `go install` in parallel.
> More information: <https://github.com/nao1215/gup#how-to-use>.

- Update all installed binaries:

`gup update`

- List all installed binaries, their package paths, and versions:

`gup list`

- Check for available updates without installing them:

`gup check`

- Export the list of installed binaries to a file:

`gup export {{[-f|--file]}} {{path/to/gup.json}}`

- Install binaries from a `gup` configuration file:

`gup import {{[-f|--file]}} {{path/to/gup.json}}`

- Remove a specific binary:

`gup remove {{binary_name}}`

- Update all binaries except for specific ones:

`gup update {{[-e|--exclude]}} {{binary1,binary2}}`

- Update specific binaries to the latest version:

`gup update --latest {{binary1,binary2}}`
