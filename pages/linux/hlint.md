# hlint

> Tool for suggesting improvements to Haskell code. These include alternative functions, simplifying code and spotting redundancies.

- To receive suggestions:

`hlint {{path/to/file}} options`

- To check all Haskell files and generate a report:

`hlint {{path/to/file}} --report`

- To automatically apply most suggestions:

`hlint {{path/to/file}} --refactor` (For additional options, do `--refactor-options`)

- To generate a settings file ignoring all outstanding hints:

`hlint {{path/to/file}} --default > .hlint.yaml` (it may be edited)


