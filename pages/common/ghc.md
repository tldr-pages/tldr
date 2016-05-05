# ghc

> The Glassgow Haskell Compiler, compiles and links Haskell source files.

- Find and compile all modules in the current directory:

`ghc Main`

- Compile a single file:

`ghc {{file.hs}}`

- Compile using optimization, for faster code:

`ghc -O {{file.hs}}`

- Stop after generating object files:

`ghc -c {{file.hs}}`

- Run in interactive mode (REPL):

`ghci`
