# ghc

> Compilatorul Glasgow Haskell.
> Compilează și leagă fișierele sursă Haskell.
> Mai multe informaţii: <https://www.haskell.org/ghc>

- Găsiți și compilați toate modulele din directorul curent:

`ghc Main`

- Compilarea unui singur fișier:

`ghc {{file.hs}}`

- Compilați folosind optimizare suplimentară:

`ghc -O {{file.hs}}`

- Opriți compilarea după generarea fișierelor obiect (.o):

`ghc -c {{file.hs}}`

- Run Haskell interpret interactiv (REPL):

`ghci`

- Evaluează o singură expresie:

`ghc -e {{expression}}`
