# cabal

> Interfaccia da linea di comando per l'infrastruttura di compilazione di Haskell (Cabal).
> Gestisce progetti Haskell e pacchetti Cabal dal repository di pacchetti Hackage.
> Maggiori informazioni: <https://cabal.readthedocs.io/en/latest/getting-started.html>.

- Cerca ed elenca pacchetti da Hackage:

`cabal list {{termine_di_ricerca}}`

- Mostra informazioni su di un pacchetto:

`cabal info {{nome_pacchetto}}`

- Scarica ed installa un pacchetto:

`cabal install {{nome_pacchetto}}`

- Crea un nuovo progetto Haskell nella directory corrente:

`cabal init`

- Compila il progetto nella directory corrente:

`cabal build`

- Esegui i test del progetto nella directory corrente:

`cabal test`
