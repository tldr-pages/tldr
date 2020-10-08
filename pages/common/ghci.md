# ghci

> The Glasgow Haskell Compiler's interactive environment.
> More information: <https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>.

- Start an interactive REPL session:

`ghci`

- Start an interactive REPL session and load the specified Haskell source file:

`ghci {{source_file.hs}}`

- Start an interactive REPL session and enable a language option:

`ghci -X{{language_option}}`

- Start an interactive REPL session and enable almost all compiler warnings:

`ghci -Wall`

- Start an interactive REPL session with a colon-separated list of directories for finding source files:

`ghci -i{{dir1:...:dirn}}`
