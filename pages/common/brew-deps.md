# brew deps

> Show dependencies for formulae and casks.
> See also: `brew leaves`.
> More information: <https://docs.brew.sh/Manpage#deps-options-formulacask->.

- Show the dependencies of a formula:

`brew deps {{formula}}`

- Show only the dependencies declared directly in a formula:

`brew deps {{[-1|--direct]}} {{formula}}`

- Show the dependencies of a formula as a tree:

`brew deps --tree {{formula}}`

- Show the dependencies shared by multiple formulae:

`brew deps {{formula1 formula2 ...}}`

- Show the dependencies of any of multiple formulae:

`brew deps --union {{formula1 formula2 ...}}`

- Include build dependencies and mark them in the output:

`brew deps --include-build --annotate {{formula}}`

- Show the dependencies of all installed formulae:

`brew deps --installed`

- Display help:

`brew deps {{[-h|--help]}}`
