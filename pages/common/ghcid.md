# ghcid

> Simple and efficient CLI IDE for Haskell that reloads code on file changes.
> Continuously displays compile errors, warnings, and test results.
> More information: <https://github.com/ndmitchell/ghcid>.

- Start `ghcid` and monitor a Haskell file for changes:

`ghcid {{path/to/Main.hs}}`

- Start `ghcid` with a specific command, such as loading a Stack or Cabal project:

`ghcid --command "{{stack ghci Main.hs}}"`

- Run an action (default `main`) on each file save:

`ghcid --run={{action}} {{path/to/Main.hs}}`

- Set maximum height and width (default to console height and width):

`ghcid --height={{height}} --width={{width}} {{path/to/Main.hs}}`

- Write full GHC compiler output to a file:

`ghcid --outputfile={{path/to/output_file.txt}} {{path/to/Main.hs}}`

- Execute REPL commands (eg. `-- $> 1+1`) on each file save:

`ghcid --allow-eval {{path/to/Main.hs}}`
