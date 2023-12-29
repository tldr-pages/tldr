# ghc

> The Glasgow Haskell Compiler.
> Compiles and links Haskell source files.
> More information: <https://www.haskell.org/ghc>.

- Find and compile all modules in the current directory:

`ghc Main`

- Compile a single file:

`ghc {{path/to/file.hs}}`

- Compile using extra optimization:

`ghc -O {{path/to/file.hs}}`

- Stop compilation after generating object files (.o):

`ghc -c {{path/to/file.hs}}`

- Start a REPL (interactive shell):

`ghci`

- Evaluate a single expression:

`ghc -e {{expression}}`
