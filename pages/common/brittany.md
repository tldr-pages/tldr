# brittany

> Pretty-print Haskell source files.
> More information: <https://github.com/lspitzner/brittany#readme>.

- Format a Haskell source file and print the result to stdout:

`brittany {{file.hs}}`

- Format all Haskell source files in the current directory in-place:

`brittany --write-mode=inplace {{*.hs}}`

- Check whether a Haskell source file needs changes; indicate the result through the exit code:

`brittany --check-mode {{file.hs}}`

- Format a Haskell source file using the specified amount of spaces per indentation level and line length:

`brittany --indent {{4}} --columns {{100}} {{file.hs}}`

- Format a Haskell source file according to the style defined in the specified config file:

`brittany --config-file {{config.yaml}} {{file.hs}}`
