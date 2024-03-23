# hlint

> Suggest improvements to Haskell code.
> More information: <http://hackage.haskell.org/package/hlint>.

- Display suggestions for a given file:

`hlint {{path/to/file}} options`

- Check all Haskell files and generate a report:

`hlint {{path/to/directory}} --report`

- Automatically apply most suggestions:

`hlint {{path/to/file}} --refactor`

- Display additional options:

`hlint {{path/to/file}} --refactor-options`

- Generate a settings file ignoring all outstanding hints:

`hlint {{path/to/file}} --default > {{.hlint.yaml}}`
