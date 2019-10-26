# hlint

> Tool for suggesting improvements to Haskell code. These include alternative functions, simplifying code and spotting redundancies.

- To receive suggestions:

`hlint {{path/to/file}} options`

- To check all Haskell files and generate a report:

`hlint {{path/to/file}} --report`

- To automatically apply most suggestions:

`hlint {{path/to/file}} --refactor`

- For additional options:

`hlint {{path/to/file}} --refactor-options`

- To generate a settings file ignoring all outstanding hints:

`hlint {{path/to/file}} --default > .hlint.yaml` 

- Documentation [here](http://hackage.haskell.org/package/hlint)
