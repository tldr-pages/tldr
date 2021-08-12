# ghci

> Mediul interactiv al compilatorului Glasgow Haskell.
> Mai multe informaţii: <https://downloads.haskell.org/ghc/latest/docs/html/users_guide/ghci.html>

- Porniți un REPL (shell interactiv):

`ghci`

- Porniți un REPL și încărcați fișierul sursă specificat Haskell:

`ghci {{source_file.hs}}`

- Porniți un REPL și activați o opțiune de limbă:

`ghci -X{{language_option}}`

- Porniți un REPL și activați un anumit nivel de avertismente de compilator (de exemplu, „toate” sau „compact”):

`ghci -W{{warning_level}}`

- Începeți un REPL cu o listă separată de două directoare pentru găsirea fișierelor sursă:

`ghci -i{{path/to/directory1}}:{{path/to/directory2}}`
