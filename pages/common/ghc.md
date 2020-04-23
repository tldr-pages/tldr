# ghc

> The Glasgow Haskell Compiler.
> Compiles and links Haskell source files.
> More information: <https://www.haskell.org/ghc>.

- Find and compile all modules in the current directory:

`ghc Main`

- Compile a single file:

`ghc {{file.hs}}`

- Compile using extra optimization:

`ghc -O {{file.hs}}`

- Stop compilation after generating object files (.o):

`ghc -c {{file.hs}}`

- Run Haskell interactive interpreter (REPL):

`ghci`

- Evaluate a single expression:

`ghc -e {{expression}}`
