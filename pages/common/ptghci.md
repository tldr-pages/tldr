# ptghci

> A REPL shell for Haskell that supports syntax highlighting, multi-line commands, etc.
> It is a wrapper around GHCi interpreter and heavily inspired by IPython.
> More information: <https://github.com/litxio/ptghci>.

- Start a REPL (interactive shell):

`ptghci`

- Run with specified Haskell library package(s) available to import:

`ptghci --package {{package1}} --package {{package2}}`

- Enter an interactive session after compiling & loading functions from a Haskell script (but NOT running `main`):

`ptghci /{{path/to/script.hs}}`

- Use a specific GHC (for example to use a specific version of the GHC Haskell compiler):

`ptghci --with-ghc /{{path/to/ghc}}`
