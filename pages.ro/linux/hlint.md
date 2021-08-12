# hlint

> Instrument pentru sugerarea îmbunătățirilor codului Haskell.
> Mai multe informaţii: <http://hackage.haskell.org/package/hlint>

- Afișați sugestii pentru un anumit fișier:

`hlint {{path/to/file}} options`

- Verificați toate fișierele Haskell și generați un raport:

`hlint {{path/to/directory}} --report`

- Aplică automat majoritatea sugestiilor:

`hlint {{path/to/file}} --refactor`

- Afișează opțiuni suplimentare:

`hlint {{path/to/file}} --refactor-options`

- Generați un fișier de setări ignorând toate sugestiile remarcabile:

`hlint {{path/to/file}} --default > {{.hlint.yaml}}`
